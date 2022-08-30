from unicodedata import category
from django.shortcuts import render
from .models import (
    Claim
)
from category.models import (
    Category,
    Products
)

def home(request):
    template = "home/home.html"

    carousel = Claim.objects.all() #for modify in 
    products = Products.objects.all()

    context = {
        "carousel":carousel,
        "products":products
    }

    return render(request, template, context)