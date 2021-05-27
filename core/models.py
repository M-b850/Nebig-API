from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                                         PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.conf import settings
import uuid


class UserManager(BaseUserManager):

    def create_user(self, email, username, password=None, **extra_fields):
        """creates and saves new user"""
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        user = self.model(
            email=self.normalize_email(email),
            username=username.lower(),
            **extra_fields
            )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """custom user model that suppers using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False
    )
    bio = models.TextField(null=True)
    followers_count = models.IntegerField(blank=True, null=True, default=0)
    followers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='following',
        blank=True
    )
    email_verified = models.BooleanField(default=False)

    class Gender(models.TextChoices):
        MALE = 'm', _('Male')
        WOMAN = 'f', _('Female')
        OTHER = 'o', _('Other')
        PNTS = 'r', _('Prefer not to say')
    gender = models.CharField(max_length=1, choices=Gender.choices)

    def __str__(self):
        return str(self.user.username)
