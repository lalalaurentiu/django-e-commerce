from django.urls import path
from .views import (
    products_by_category,
    products_by_brands,
    product
)

app_name = "category"

urlpatterns = [
    path("product/<product_slug>", product, name="product"),
    path("<slug>", products_by_category, name="products_category"),
    path("<category_brand>/<category_slug>", products_by_brands, name="product_brands"),
    
]