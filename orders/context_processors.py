from .cart import Cart
from .forms import CartAddProductForm

def cart(request):
    add = CartAddProductForm()
    context = {
        "cart":Cart(request),
        "add_to_cart":add
    }
    return context
