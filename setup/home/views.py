from unicodedata import category
from django.shortcuts import render
from .models import (
    Claim
)
from category.models import (
    Category
)

def home(request):
    template = "home/home.html"

    claims = Claim.objects.all()
    categorys = Category.objects.all()

    context = {
        "claims":claims,
        # "categorys":categorys
    }

    return render(request, template, context)