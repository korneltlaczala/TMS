from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login(request):
    return render(request, 'user/login.html')

def register(request):
    return render(request, 'user/register.html')

def password_reset(request):
    return render(request, 'user/password_reset.html')