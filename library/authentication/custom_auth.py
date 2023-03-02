from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from .models import CustomUser

User = get_user_model()

class CustomUserAuthBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(email=email)
            print(user.password)
            if user.password == password:
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, id):
        try:
            return CustomUser.objects.get(pk=id)
        except CustomUser.DoesNotExist:
            return None