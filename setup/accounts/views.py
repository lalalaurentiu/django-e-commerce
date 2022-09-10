from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

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
