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
    # Fields to display in the list view
    list_display = [
        "title",
        "author",
        "description",
        "publication_date",
        "isbn",
        "price",
        "user",
    ]

    # Fields to search in the admin interface
    search_fields = ["title", "author", "isbn", "user__username"]

    # Filters to display in the right sidebar
    list_filter = ["publication_date", "author", "price"]

    # Default ordering of the list view
    ordering = ["title"]

    # Fields that can be edited directly in the list view
    list_editable = ["price"]

    # Fields that are read-only in the form view
    # readonly_fields = ["isbn"]

    # Organize fields into sections in the form view
    fieldsets = (
        (None, {
            "fields": ("title", "author", "description", "publication_date", "isbn", "price", "cover_image", "user")
        }),
        ("Advanced options", {
            "classes": ("collapse",),
            "fields": (),
        }),
    )

    # Display a raw ID widget for the user field
    raw_id_fields = ["user"]

    # Add autocomplete functionality for the user field
    autocomplete_fields = ["user"]

    # Add a date-based drill-down navigation by publication date
    date_hierarchy = "publication_date"

    # Automatically populate the ISBN field based on the title
    prepopulated_fields = {"isbn": ("title",)}


# Register the Books model with the BookAdmin configuration
admin.site.register(Books, BookAdmin)
