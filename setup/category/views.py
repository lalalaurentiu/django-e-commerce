
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Products, Category, Brands

def products_by_category(request, slug ):
    template = "category/category_products.html"
    category = get_object_or_404 (Category, slug = slug)
    products = Products.objects.filter(category = category)
    context = {
        "products":products
    }

    return render(request, template, context)

def products_by_brands(request, category_brand, category_slug):
    template = "category/brand_products.html"
    
    try:
        brand = Brands.objects.filter(slug = category_brand).values_list("id", flat=True)[0]
        category = Category.objects.filter( brands = brand, slug = category_slug).values_list("id", flat=True)[0]
        products = Products.objects.filter(brand=brand, category = category)
        context = {
            "products":products
        }

        return render(request, template, context)
    except:
        raise Http404

def product(request, product_slug):
    template = "category/product.html"
    products = Products.objects.prefetch_related("productDetails")
    product = get_object_or_404(products, slug=product_slug)

    context = {
        "product":product
    }

    return render(request ,template ,context )