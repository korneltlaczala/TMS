from django.db import IntegrityError
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse

# Create your views here.

def login(request):
    return render(request, 'user/login.html')

def choose_account_type(request):
    return render(request, 'user/choose_account_type.html')

def register(request, type=None):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        if User.objects.filter(email=email).exists():
            return render(request, 'user/register.html', {
                "type": type,
                "message": "We already have an account with this email! Maybe try to log in instead."
            })
        
        if User.objects.filter(username=username).exists():
            return render(request, 'user/register.html', {
                "type": type,
                "message": "Username already exists! Please try a different one."
            })
        
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.is_active = False
            user.save()

            return HttpResponseRedirect(reverse('confirm_email'))

        except IntegrityError as e:
            return render(request, 'user/register.html', {
                "type": type,
                "message": "Could not create user! Please try again."
            })

def register_coach(request):
    type = 'coach'
    context = {'type': type}
    return render(request, 'user/register.html', context)

def register_parent(request):
    type = 'parent'
    context = {'type': type}
    return render(request, 'user/register.html', context)

def register_player(request):
    type = 'player'
    context = {'type': type}
    return render(request, 'user/register.html', context)

def password_reset(request):
    return render(request, 'user/password_reset.html')

def confirm_email(request):
    return render(request, 'user/confirm_email.html')

def terms(request):
    return render(request, 'user/terms.html')
