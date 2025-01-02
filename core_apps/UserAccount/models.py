from django.contrib.auth.models import AbstractUser
from django.db import models


class UserAccount(AbstractUser):
    email = models.EmailField(unique=True)

    class Meta:
        db_table = "user_account"

    def __str__(self):
        return self.email if self.email else self.username


class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cover_image = models.ImageField(upload_to="book_covers/", blank=True, null=True)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
