"""Test auth API."""

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


class UserAPICase(TestCase):
    """Class for testing auth API."""

    def setUp(self):
        """Set up objects for test auth API."""
        self.client = APIClient()
        self.email = 'test@extend.tv'
        self.password = 'test'

    def create_user(self):
        """Create new user."""
        user = get_user_model().objects.create(email=self.email, is_active=True)
        user.set_password(self.password)
        user.save(update_fields=['password'])
        return user

    def test_unauthenticated_access_to_private_endpoint(self):
        """Request to private_health endpoint by unauthenticated user."""
        response = self.client.get('/api/health_private/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_access_to_private_endpoint(self):
        """Request to private_health endpoint by authenticated user."""
        self.create_user()

        response = self.client.post(reverse('token-obtain'), data={'email': self.email, 'password': self.password})
        self.assertIn('access', response.data)

        self.access_token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        response = self.client.get('/api/health_private/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
