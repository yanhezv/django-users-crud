from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom user model extending Django's AbstractUser.
    Ready for future extensions.
    """

    email = models.EmailField(unique=True)

    REQUIRED_FIELDS = ["email"]

    def __str__(self) -> str:
        return self.username
