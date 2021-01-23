from django.db import models


LANGUAGE_CHOICES = (
    ('fa', 'Farsi'),
    ('en', 'English'),
)
QTE_CHOICES = (
    ('va', 'vaziri'),
    ('rq', 'roqei'),
)
JELD_CHOICES = (
    ('sm', 'Shomiz'),
    ('gl', 'galingor'),
)


class Author(models.Model):
    # Author Model

    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=50)
    bio = models.TextField(max_length=4000)
    photo = models.ImageField(upload_to='photos/pro')
    # awards =
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def __str__(self):
        return f"{self.last_name} {self.name}"


class Translator(models.Model):
    # Translator Model

    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=50)
    bio = models.TextField(max_length=4000)
    photo = models.ImageField(upload_to='photos/pro')
    # awards =
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def __str__(self):
        return f"{self.last_name} {self.name}"


class Publisher(models.Model):
    name = models.CharField(max_length=40)


class Book(models.Model):
    # Book Model with attributes

    title = models.CharField(max_length=40)
    slug = models.SlugField(max_length=40, unique=True, null=True, blank=True)
    sub_title = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=4000)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    translator = models.ForeignKey('Translator', on_delete=models.SET_NULL, null=True)
    cover = models.ImageField(upload_to='photos/covers')
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2)
    # size --> height against the width of a leaf, or sometimes -
    # the height and width of its cover.
    size = models.CharField(choices=QTE_CHOICES, max_length=2)
    cover_type = models.CharField(choices=JELD_CHOICES, max_length=2)
    # number of pages
    pages = models.IntegerField()
    rate = models.FloatField()
    # International Standard Book Number
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title


'''
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"{self.user} - {self.created_on}"
'''