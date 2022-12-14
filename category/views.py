from django.shortcuts import render, get_object_or_404, get_list_or_404, HttpResponse
from .models import *
from django.db.models import FilteredRelation
from django.contrib import messages
from accounts.models import CustomUser
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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

    page_num = request.GET.get('page', 1)
    paginator = Paginator(products, 8)

    try:
        products = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        products = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        products = paginator.page(paginator.num_pages)

    context = {
        "products":products,
        "section":section,
    }

    return render(request, template, context)

def products_by_brands(request, category_brand, category_slug):

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
    
    page_num = request.GET.get('page', 1)
    paginator = Paginator(products, 8)

    try:
        products = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        products = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        products = paginator.page(paginator.num_pages)

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
    user = CustomUser.objects.get(id = request.user.id)
    product = Products.objects.get(id = request.POST["product"])
    star = request.POST["star"]
    message = request.POST["message"]

    # try:
    instance = ProductRaiting.objects.create(
        user=user,
        product=product,
        raiting=star,
        message=message
    )
    instance.save()
    # except:
    #     pass
    messages.success(request,"Thanks for raiting")
    return HttpResponse(200)