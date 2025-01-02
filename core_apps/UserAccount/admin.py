from django.contrib import admin
from .models import UserAccount


class UserAdmin(admin.ModelAdmin):
    list_display = [
        "email",
        "username",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
        "is_superuser",
        "date_joined",
        "last_login",
    ]

    search_fields = ["email", "username", "first_name", "last_name"]


admin.site.register(UserAccount, UserAdmin)
