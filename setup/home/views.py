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

    claims = Claim.objects.all()
    products = Products.objects.all()

    context = {
        "claims":claims,
        "products":products
    }

    return render(request, template, context)