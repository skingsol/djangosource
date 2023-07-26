from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    # http://127.0.0.1:8000/users/
    path("", views.user_main, name="main"),
    # http://127.0.0.1:8000/register/
    path("register/", views.signup, name="register"),
    # http://127.0.0.1:8000/login/
    path("login/", views.common_login, name="login"),
        # http://127.0.0.1:8000/login/
    path("logout/", views.common_logout, name="logout"),
]
