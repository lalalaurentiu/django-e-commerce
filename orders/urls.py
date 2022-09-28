from django.urls import path
from .views import *

app_name = "cart"

urlpatterns = [
    path("", cart, name="cart"),
    path("checkout", Checkout.as_view(), name="checkout"),
    path("download/<int:order_id>", generatePdf, name="download"),
    path('add/<int:product_id>/', cart_add, name='cart_add'),
    path('decrease/<int:product_id>/', cart_decrease, name='cart_decrease'),
    path('remove/<int:product_id>/', cart_remove, name='cart_remove'),
]