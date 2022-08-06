from django.db import models
from django.contrib.auth.models import AbstractUser

from core.managers import CustomUserManager

# Create your models here.

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.email