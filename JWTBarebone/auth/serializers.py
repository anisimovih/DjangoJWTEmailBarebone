from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenVerifySerializer


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField()


class TokenSerializerResponse(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()


class LightTokenSerializerResponse(serializers.Serializer):
    access = serializers.CharField()


class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = get_user_model().EMAIL_FIELD


class CustomTokenVerifySerializer(TokenVerifySerializer):
    """Return code 400 instead of 401 for invalid token."""

    def validate(self, attrs):
        try:
            return super().validate(attrs)
        except TokenError as exception:
            raise serializers.ValidationError(exception)
