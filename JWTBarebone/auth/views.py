"""Auth views."""

from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView


from .serializers import EmailTokenObtainPairSerializer, TokenSerializerResponse


@method_decorator(name='post', decorator=swagger_auto_schema(responses={200: TokenSerializerResponse()}))
class EmailTokenObtainPairView(TokenObtainPairView):
    """TokenObtainPairView with custom serialiser."""

    serializer_class = EmailTokenObtainPairSerializer


class PublicApiHealthView(APIView):
    """Health check with public access."""

    permission_classes = [AllowAny]

    def get(self, request):
        """Return ok if server is alive."""
        return Response('OK')


class PrivateApiHealthView(APIView):
    """Health check with private access."""

    def get(self, request):
        """Return ok if server is alive."""
        return Response('OK')
