from django.contrib.auth.models import AbstractUser
from django.db import models


class UserAccount(AbstractUser):
    email = models.EmailField(unique=True)

    class Meta:
        db_table = "user_account"

    def __str__(self):
        return self.email if self.email else self.username
