from .models import (
    Category,
    Products
)

def items(request):
    categorys = Category.objects.all()
    products = Products.objects.all()

    context = {
        "categorys":categorys,
    }

    return context