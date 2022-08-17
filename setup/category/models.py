from django.db import models 

# change 
# from django.utils.translation import ugettext as _ 
# whith
# from django.utils.translation import gettext_lazy as _
# in 
# C:\Users\username\Desktop\Programare\e-commerce\e-commerce-env\Lib\site-packages\ fontawesome_5\ fields.py
from fontawesome_5.fields import IconField

class Category(models.Model):
    title = models.TextField(max_length=100)
    image = IconField()
    svg = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

class Brands(models.Model):
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE, related_name="categorys")
    title = models.TextField(max_length=50)

    def __str__(self):
        return self.title

class Products(models.Model):
    brand = models.ForeignKey(Brands, null=True, on_delete=models.CASCADE, related_name="brands")
    name = models.TextField(max_length=100)
    description = models.TextField()
    details = models.TextField()
    image = models.ImageField(upload_to = "images/Products")
    price = models.DecimalField(max_digits = 5, decimal_places = 2)