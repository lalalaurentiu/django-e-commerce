from django.urls import path, re_path
from .views import *

app_name = "home"
dispach = lambda path : path if "popularity" in path else ""
urlpatterns = [
    path("", home, name="home"),
    path("popularity", home, name="homePopularity"),
]