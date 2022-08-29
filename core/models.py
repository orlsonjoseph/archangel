from django.db import models
from django.db.models.signals import post_save

from django.conf import settings
from django.contrib.auth.models import AbstractUser

from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from core.managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None

    email = models.EmailField(('email address'), unique=True)
    email_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.email


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
