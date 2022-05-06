from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    point = models.IntegerField(default=0, blank=True)

