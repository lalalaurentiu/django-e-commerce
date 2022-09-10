from django.urls import path
from django.contrib.auth.views import(
    LoginView,
    LogoutView
) 
from .forms import *

app_name = "accounts"

urlpatterns = [
    path("login/", LoginView.as_view(form_class = CustomAuthentificationForm ,template_name = "accounts/login.html"), name="login"),
]