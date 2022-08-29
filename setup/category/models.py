from django.db import models 

# change 
# from django.utils.translation import ugettext as _ 
# whith
# from django.utils.translation import gettext_lazy as _
# in 
# C:\Users\username\Desktop\Programare\e-commerce\e-commerce-env\Lib\site-packages\ fontawesome_5\ fields.py
from fontawesome_5.fields import IconField

class Brands(models.Model):
    title = models.TextField(max_length=50)

    def __str__(self):
        return self.title

class Category(models.Model):
    brands = models.ManyToManyField(Brands ,related_name="brands")
    title = models.TextField(max_length=100)
    image = IconField()
    svg = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

class Products(models.Model):
    brand = models.ForeignKey(Brands, null=True, on_delete=models.CASCADE, related_name="productBrands")
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE, related_name="productsCategory")
    name = models.TextField(max_length=100)
    description = models.TextField()
    details = models.TextField()
    image = models.ImageField(upload_to = "images/Products")
    price = models.DecimalField(max_digits = 5, decimal_places = 2)
    discount = models.FloatField(default=0)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = self.name.replace(" ", "_")
        super(Products, self).save(*args, **kwargs)