from django.shortcuts import render
from .models import (
    Claim
)
from category.models import *

def home(request):
    template = "home/home.html"

    carousel = Claim.objects.all() #for modify in 
    
    if "popularity" in request.path :
        products = Products.objects.prefetch_related("productRaiting").order_by("-productRaiting")
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