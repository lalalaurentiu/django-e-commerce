from django.shortcuts import render, get_object_or_404, get_list_or_404, HttpResponse
from .models import *
from django.db.models import FilteredRelation
from django.contrib import messages

def products_by_category(request, slug ):

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

    print(request.path)
    template = "category/brand_products.html"
    section = "all"
    
    try:
        brand = Brands.objects.filter(slug = category_brand).values_list("id", flat=True)[0]
        category = Category.objects.filter( brands = brand, slug = category_slug).values_list("id", flat=True)[0]
        
    except:
        brand = None
        category = None
    products = get_list_or_404(Products, brand=brand, category = category)

    try:
        if "low" in request.GET["args"]:
            products =Products.objects.filter(brand=brand ,category = category).order_by("price")
            section = "low"
        elif "hight" in request.GET["args"]:
            products =Products.objects.filter(brand=brand, category = category).order_by("-price")
            section = "hight"
        elif "popularity" in request.GET["args"]:
            products = Products.objects.filter(brand=brand, category = category).prefetch_related("productRaiting").order_by("-productRaiting")
            section = "popularity"

        raiting_filters = {
            "starone":Products.objects.filter(
                brand=brand,
                category = category
                ).annotate(
                    products = FilteredRelation(
                        "productRaiting" 
                        )
                    ).filter(products__raiting = 1),
            "startwo":Products.objects.filter(
                brand=brand,
                category = category
                ).annotate(
                    products = FilteredRelation(
                        "productRaiting" 
                        )
                    ).filter(products__raiting = 2),
            "starthree":Products.objects.filter(
                brand=brand,
                category = category
                ).annotate(
                    products = FilteredRelation(
                        "productRaiting" 
                        )
                    ).filter(products__raiting = 3),
            "starfour":Products.objects.filter(
                brand=brand,
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
        "section":section
    }

    return render(request, template, context)

def product(request, product_slug):
    template = "category/product.html"
    product = get_object_or_404(Products, slug=product_slug)

    context = {
        "product":product
    }

    return render(request ,template ,context )

def raiting(request):
    print(request.POST)
    product = Products.objects.get(id = request.POST["product"])
    star = request.POST["star"]
    message = request.POST["message"]

    # try:
    instance = ProductRaiting.objects.create(
        product=product,
        raiting=star,
        message=message
    )
    instance.save()
    # except:
    #     pass
    messages.success(request,"Thanks for raiting")
    return HttpResponse(200)