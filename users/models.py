from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from rest_framework.authentication import TokenAuthentication


class User(AbstractUser):
    point = models.IntegerField(default=0, blank=True)
    objects = UserManager()

    def __str__(self):
        return self.username


class BearerTokenAuthentication(TokenAuthentication):
    keyword = 'Bearer'
