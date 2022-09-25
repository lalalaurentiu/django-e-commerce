from django.shortcuts import render
from .models import (
    Claim
)
from category.models import *

def home(request):
    template = "home/home.html"

    carousel = Claim.objects.all() #for modify in 
    
    if "popularity" in request.path :
        all_products = Products.objects.prefetch_related("productRaiting").order_by("-productRaiting")
        products = []
        for product in all_products:
            if product not in products:
                products.append(product)
        section = "popularity"
    else:
        products = Products.objects.all()
        section = "all"
    context = {
        "carousel":carousel,
        "products":products,
        "section":section
    }

    return render(request, template, context)