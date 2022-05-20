from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

UserModel = get_user_model()


class EmailBackend(ModelBackend):
    """Auth user backend that uses email instead of username."""

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            email = kwargs.get(UserModel.EMAIL_FIELD)
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None
