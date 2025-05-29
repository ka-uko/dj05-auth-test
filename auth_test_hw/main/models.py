from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number = models.CharField("Номер телефона", max_length=15, blank=True, unique=True)
    email = models.EmailField(unique=True)

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"
