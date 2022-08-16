from django.shortcuts import render
from .models import (
    Claim
)

def home(request):
    template = "home/home.html"
    claims = Claim.objects.all()

    context = {
        "claims":claims
    }
    
    return render(request, template, context)