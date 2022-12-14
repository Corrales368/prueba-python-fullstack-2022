# Import django
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Override user django default.
    """
    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = ["email", "first_name"]
