from django.shortcuts import render
from .models import UserModel, UserDataModel

def index(request):
    return render(request, "authapp/wellcome.html", context={})