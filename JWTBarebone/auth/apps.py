"""Root point for auth app."""
from django.apps import AppConfig


class AuthConfig(AppConfig):
    """Main auth app class."""

    name = 'JWTBarebone.auth'
    label = 'JWTBarebone_auth'
