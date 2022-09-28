from django.db import models
from category.models import Products

class Claim(models.Model):
    choices = [
        ("subtraction", "subtraction"),
        ("percent", "percent")
    ]
    products = models.ManyToManyField(Products, related_name="deals")
    image = models.ImageField(upload_to = "images/Claim")
    title = models.TextField(max_length=250)
    description = models.TextField()
    deal_choices = models.CharField(choices=choices, max_length=11)
    deal_sum = models.IntegerField()

    def __str__(self):
        return self.title
