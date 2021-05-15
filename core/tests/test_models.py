from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='test@example.com',
                username='Abbas',
                password='Testpassword'):
    """Create a sample user"""
    return get_user_model().objects.create_user(username, email, password)


class ModelTest(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@example.com'
        username = 'Abbirezaa'
        password = 'Testme123'
        user = get_user_model().objects.create_user(
            email=email,
            username=username,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertEqual(user.username, username.lower())
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for new user is normalized"""
        email = 'test@EXAMPLE.com'
        print(email.lower())
        user = get_user_model().objects.create_user(email, 'Testme123')

        self.assertEqual(user.email, email.lower())

    def test_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Testme123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'Testme123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
