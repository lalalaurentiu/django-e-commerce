from django.shortcuts import render
from .models import (
    Claim
)
from category.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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

    page_num = request.GET.get('page', 1)

    paginator = Paginator(products, 9)

    try:
        products = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        products = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        products = paginator.page(paginator.num_pages)

    context = {
        "carousel":carousel,
        "products":products,
        "section":section
    }

    return render(request, template, context)