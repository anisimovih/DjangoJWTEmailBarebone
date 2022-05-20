from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView


from .serializers import (
    CustomTokenVerifySerializer,
    EmailTokenObtainPairSerializer,
    TokenSerializerResponse,
)


@method_decorator(name='post', decorator=swagger_auto_schema(responses={200: TokenSerializerResponse()}))
class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer


@method_decorator(name='post', decorator=swagger_auto_schema(responses={200: serializers.Serializer()}))
class TokenVerifyView(TokenVerifyView):
    serializer_class = CustomTokenVerifySerializer


class PublicApiHealthView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response('OK')


class PrivateApiHealthView(APIView):

    def get(self, request):
        return Response('OK')
