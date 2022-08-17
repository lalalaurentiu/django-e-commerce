from django.contrib import admin

from .models import (
    Category,
    Brands,
    Products
)

admin.site.register(Category)
admin.site.register(Brands)
admin.site.register(Products)