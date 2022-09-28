from django.contrib import admin

from .models import *

admin.site.register(Category)
admin.site.register(Brands)
admin.site.register(Products)
admin.site.register(ProductsDetails)
admin.site.register(ProductRaiting)
admin.site.register(ProductImages)