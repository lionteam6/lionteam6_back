from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    name = models.CharField(max_length=30)
    university = models.CharField(max_length=50)
    nickname = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.username