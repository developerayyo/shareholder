from django.contrib.auth.decorators import login_required
from django.urls import include
from django.urls import path
from django.urls import re_path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("shareholders/", views.shareholders, name="shareholders"),
]
