from django.contrib import admin
from .models import UserAccount, Books


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


class BookAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "author",
        "description",
        "publication_date",
        "isbn",
        "price",
    ]

    search_fields = ["title", "author", "isbn"]


admin.site.register(Books, BookAdmin)
