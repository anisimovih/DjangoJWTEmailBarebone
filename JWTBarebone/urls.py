"""JWTBarebone URL Configuration"""
import debug_toolbar
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenRefreshView

from JWTBarebone.auth.views import (
    EmailTokenObtainPairView,
    TokenVerifyView,
    PublicApiHealthView,
    PrivateApiHealthView
)

JWTBarebone_info = openapi.Info(
    title='JWT Barebone API',
    default_version='v1',
    license=openapi.License(name='Apache 2.0')
)
schema_view = get_schema_view(
    JWTBarebone_info,
    permission_classes=(permissions.AllowAny,),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # API
    path('api/auth/token/', EmailTokenObtainPairView.as_view(), name='token-obtain'),
    path('api/auth/token/verify/', TokenVerifyView.as_view(), name='token-verify'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('api/health/', PublicApiHealthView.as_view(), name='api-health'),
    path('api/health_private/', PrivateApiHealthView.as_view(), name='api-health-private'),

    # API documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),

    path('__debug_toolbar__/', include(debug_toolbar.urls)),
]
