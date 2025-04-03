from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserAccount(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    def __str__(self):
        return self.first_name + " " + self.last_name
