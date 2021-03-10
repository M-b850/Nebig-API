from rest_framework import serializers

from core.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for Author objects"""

    class Meta:
        model = Author
        fields = (
            'id',
            'name',
            'last_name',
            'profile',
            'date_of_birth',
            'date_of_death',
        )
        read_only_fields = ('id',)
