from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from orders.models import Order

def register(request):
    template_name = "accounts/register.html"
    registerForm = CustomUserCreationForm()

    if request.method == "POST":
        registerForm = CustomUserCreationForm(request.POST)
        if registerForm.is_valid():
            registerForm.save()
            return redirect("accounts:login")
    else:
        registerForm = CustomUserCreationForm()

    context = {
        "form": registerForm,
    }
    
    return render(request, template_name, context)

@login_required
def downloadOrders(request):
    template = "accounts/orders.html"
    orders = Order.objects.filter(user_id = request.user.id)
    context = {
        "orders":orders
    }
    return render(request, template, context)
