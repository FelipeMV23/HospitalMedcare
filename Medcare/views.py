from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'login.html')

def quienes_somos(request):
    return render(request, 'quienes_somos.html')