"""Custom backends."""

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

UserModel = get_user_model()


class EmailBackend(ModelBackend):
    """Auth user backend that uses email instead of username."""

    def authenticate(self, request, username=None, password=None, **kwargs):
        """Custom authenticate to use email instead of username."""
        if username is None:
            username = kwargs.get(UserModel.EMAIL_FIELD)
        if username is None or password is None:
            return
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            UserModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
