from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login(request):
    return render(request, 'user/login.html')

def register(request):
    return render(request, 'user/register.html')

def password_reset(request):
    return render(request, 'user/password_reset.html')

def register_coach(request):
    return render(request, 'user/register_coach.html')

def register_parent(request):
    return render(request, 'user/register_parent.html')

def register_player(request):
    return render(request, 'user/register_player.html')

def players(request):
    return render(request, 'user/players.html')