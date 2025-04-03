from django.contrib import admin
from .models import UserAccount

# Register your models here.

admin.site.site_header = "User Account Management"

admin.site.register(UserAccount)
