from django.urls import path
from .views import detail, info

app_name = "app1"

urlpatterns = [
    path("",detail, name="detail"),
    path("info/", info, name="info"),
]
