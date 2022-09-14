from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import Http404
from .models import *
from django.db.models import FilteredRelation, Q
def products_by_category(request, slug ):
    # print("low" in request.GET["args"])

    print(request.path)
    template = "category/category_products.html"
    category = get_object_or_404 (Category, slug = slug)
    products = Products.objects.filter(category = category)
    section = "all"

    try:
        if "low" in request.GET["args"]:
            products =Products.objects.filter(category = category).order_by("price")
            section = "low"
        elif "hight" in request.GET["args"]:
            products =Products.objects.filter(category = category).order_by("-price")
            section = "hight"
        elif "popularity" in request.GET["args"]:
            products = Products.objects.filter(category = category).prefetch_related("productRaiting").order_by("-productRaiting")
            section = "popularity"

        raiting_filters = {
            "starone":Products.objects.filter(
                category = category
                ).annotate(
                    products = FilteredRelation(
                        "productRaiting" 
                        )
                    ).filter(products__raiting = 1),
            "startwo":Products.objects.filter(
                category = category
                ).annotate(
                    products = FilteredRelation(
                        "productRaiting" 
                        )
                    ).filter(products__raiting = 2),
            "starthree":Products.objects.filter(
                category = category
                ).annotate(
                    products = FilteredRelation(
                        "productRaiting" 
                        )
                    ).filter(products__raiting = 3),
            "starfour":Products.objects.filter(
                category = category
                ).annotate(
                    products = FilteredRelation(
                        "productRaiting" 
                        )
                    ).filter(products__raiting = 4),
        }
        for key, values in raiting_filters.items():
            if key == request.GET["args"]:
                products = values
                section = key

    except:
        pass

    context = {
        "products":products,
        "section":section,
    }

    return render(request, template, context)

def products_by_brands(request, category_brand, category_slug):
    template = "category/brand_products.html"
    
    try:
        brand = Brands.objects.filter(slug = category_brand).values_list("id", flat=True)[0]
        category = Category.objects.filter( brands = brand, slug = category_slug).values_list("id", flat=True)[0]
    except:
        brand = None
        category = None
    products = get_list_or_404(Products, brand=brand, category = category)
    context = {
        "products":products
    }

    return render(request, template, context)

def product(request, product_slug):
    template = "category/product.html"
    product = get_object_or_404(Products, slug=product_slug)

    context = {
        "product":product
    }

    return render(request ,template ,context )