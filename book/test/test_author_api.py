from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Author

from book.serializers import AuthorSerializer


AUTHOR_URL = reverse('book:author-list')


class PublicAuthorTests(TestCase):
    """Test the publicly Authors available API"""

    def SetUp(self):
        self.client = APIClient()

    def test_author_list_available(self):
        """Test that Authors List is available publicly"""
        Author.objects.create(
            name='Friedrich',
            last_name='Nietzsche',
            about='He was cool.',
            profile=None,
            date_of_birth=None,
            date_of_death=None
        )
        Author.objects.create(
            name='Baruch',
            last_name='Spinoza',
            about='He was madly alone.',
            profile=None,
            date_of_birth=None,
            date_of_death=None
        )
        res = self.client.get(AUTHOR_URL)
        serializer = Author.objects.all()

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), len(serializer))
