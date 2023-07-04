from typing import Any, Optional
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.http.request import HttpRequest
from .models import User

class ValidateMyBackend(BaseBackend):
    def authenticate(self, username=None, password=None):
        print('entre al autenticate')
        try:
            user = User.objects.get(username=username)
            if user.password == password:
                print('usuario existe')
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None