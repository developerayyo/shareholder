from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
@login_required
def home(request):
    return render(request, "account/home.html")


@login_required
def shareholders(request):
    return render(request, "shareholders.html")
