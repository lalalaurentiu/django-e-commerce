from django.db import models 
from django.urls import reverse 

# change 
# from django.utils.translation import ugettext as _ 
# whith
# from django.utils.translation import gettext_lazy as _
# in 
# C:\Users\username\Desktop\Programare\e-commerce\e-commerce-env\Lib\site-packages\ fontawesome_5\ fields.py
from fontawesome_5.fields import IconField

class Brands(models.Model):
    title = models.TextField(max_length=50)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = self.title.replace(" ", "_")
        super(Brands, self).save(*args, **kwargs)

class Category(models.Model):
    brands = models.ManyToManyField(Brands ,related_name="brands")
    title = models.TextField(max_length=100)
    image = IconField()
    svg = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def get_absolute_url(self):
        pass

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = self.title.replace(" ", "_")
        super(Category, self).save(*args, **kwargs)

class Products(models.Model):
    brand = models.ForeignKey(Brands, null=True, on_delete=models.CASCADE, related_name="productBrands")
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE, related_name="productsCategory")
    name = models.TextField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    discount = models.FloatField(default=0)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category:product',  args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = self.name.replace(" ", "-")
        super(Products, self).save(*args, **kwargs)

class ProductsDetails(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE, related_name="productDetails")
    detail_name = models.CharField(max_length=50)
    detail_value = models.CharField(max_length=100)

    def __str__(self):
        return self.product.name + " " + self.detail_name

class ProductRaiting(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE, related_name="productRaiting")
    raiting = models.DecimalField(default = 5, max_digits=2, decimal_places=1)

    def __str__(self):
        return self.product.name + " " + str(self.raiting)

class ProductImages(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE, related_name="productImages")
    image = models.ImageField(upload_to = "images/Products")

    def __str__(self):
        return self.product.name + " " + "Image"