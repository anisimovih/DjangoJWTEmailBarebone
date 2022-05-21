"""Auth serializers."""

from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class TokenSerializerResponse(serializers.Serializer):
    """Token serializer for swagger."""

    access = serializers.CharField()
    refresh = serializers.CharField()


class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    """EmailToken serializer for swagger."""

    username_field = get_user_model().EMAIL_FIELD
