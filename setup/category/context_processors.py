from .models import (
    Category
)

def items(request):
    categorys = Category.objects.all()

    context = {
        "categorys":categorys
    }

    return context