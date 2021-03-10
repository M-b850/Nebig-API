from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser

from core.models import Author

from book import serializers


class AuthorViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """Manage Author in the database"""
    queryset = Author.objects.all()
    serializer_class = serializers.AuthorSerializer
