from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def index(request):

    auth.logout(request)
    return redirect('home')