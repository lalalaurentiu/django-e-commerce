from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from category.models import Products
from .cart import Cart
from .forms import *
from django.views.decorators.csrf import requires_csrf_token
from django.views.generic import TemplateView, View
from django.contrib import messages
from .models import *
from .process import html_to_pdf 
from django.contrib.auth.decorators import login_required


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

class Checkout(TemplateView):
    template = "cart/checkout.html"
    context = {}

    def get(self, request):
        checkout = CheckoutForm()
        self.context["form"] = checkout
        self.context["errors"] = False
        return render(request, self.template, self.context)

    def post(self, request):
        cart = Cart(request)
        checkoutform = CheckoutForm(request.POST)
        if request.method == "POST":
            if checkoutform.is_valid():
                if request.user.id:
                    checkout = checkoutform.save(commit=False)
                    checkout.user_id = request.user.id
                    checkout.save()
                else:
                    checkout = checkoutform.save()
                for item in cart:
                    OrderItem.objects.create(
                        order_id = checkout.pk,
                        product_id = item["product"].id,
                        quantity = item["quantity"],
                        price = item["quantity"] * item["price"]
                        )
                cart.clear()
                messages.success(request, "Your order has been placed" )
                return redirect("home:home")          
            else:
                self.context["form"] = CheckoutForm(request.POST)
                self.context["errors"] = True
                return render(request, self.template, self.context)
        else:
            self.context["form"] = CheckoutForm()
               

@requires_csrf_token
@require_POST
def cart_add(request, product_id):
    print(request.path_info)
    cart = Cart(request)
    product = get_object_or_404(Products, id=product_id)
    form = CartAddProductForm(request.POST)
    print(form.errors)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=1,
                 override_quantity=cd['override'])
    return HttpResponse(status = 100)

def cart_decrease(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Products, id=product_id)
    form = CartDecreaseProductForm(request.POST)
    print(form.errors)
    if form.is_valid():
        cart.decrease(product=product)
    return HttpResponse(status = 100)


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Products, id=product_id)
    cart.remove(product)
    return HttpResponse(status = 100)




@login_required
def generatePdf(request, order_id):
    template = "order/download.html"
    data = OrderItem.objects.filter(order_id = order_id)
    context = {
        "data":data
    }

    pdf = html_to_pdf(template, context_dict = context)

    return HttpResponse(pdf, content_type='application/pdf')

