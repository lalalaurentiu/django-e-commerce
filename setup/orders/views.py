from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from category.models import Products
from .cart import Cart
from .forms import CartAddProductForm, CartDecreaseProductForm
from django.views.decorators.csrf import requires_csrf_token

def cart(request):
    cart = Cart(request)
    template = "cart/cart.html"
    
    add_item_form = CartAddProductForm()
    decrease_item_form = CartDecreaseProductForm()

    context = {
        "cart":cart,
        "add":add_item_form,
        "decrease":decrease_item_form
    }
    return render(request, template, context)



@requires_csrf_token
@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Products, id=product_id)
    form = CartAddProductForm(request.POST)
    print(form.errors)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=1,
                 override_quantity=cd['override'])
    return HttpResponse(status = 204)

def cart_decrease(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Products, id=product_id)
    form = CartDecreaseProductForm(request.POST)
    print(form.errors)
    if form.is_valid():
        cart.decrease(product=product)
    return HttpResponse(status = 204)


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Products, id=product_id)
    cart.remove(product)
    return HttpResponse(status = 204)

