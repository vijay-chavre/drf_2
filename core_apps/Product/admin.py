from django.contrib import admin

from .models import Product, Category, Supplier

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "price",
        "description",
        "image",
    ]


admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "description",
    ]


admin.site.register(Category, CategoryAdmin)


class SupplierAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "email",
        "phone",
        "address",
    ]


admin.site.register(Supplier, SupplierAdmin)
