from django.db import IntegrityError
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from django.contrib.auth import get_user_model, logout

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
        agree = request.POST.get('agree')

        if User.objects.filter(email=email).exists():
            return render(request, 'user/register.html', {
                "type": type,
                "message": "We already have an account with this email! Maybe try to log in instead.",
                "username": username,
                "password": password,
                "agree": agree,
            })
        
        if User.objects.filter(username=username).exists():
            return render(request, 'user/register.html', {
                "type": type,
                "message": "Username already exists! Please try a different one.",
                "email": email,
                "password": password,
                "agree": agree,
            })
        
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            mail_subject = "Activate your TMS account."
            message = render_to_string('user/acc_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user), 
            })
            email_message = EmailMessage(mail_subject, message, to=[email])
            email_message.send()
            return HttpResponseRedirect(reverse('confirm_email'))

        except IntegrityError as e:
            return render(request, 'user/register.html', {
                "type": type,
                "message": "Could not create user! Please try again.",
                "username": username,
                "email": email,
                "password": password,
                "agree": agree,
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

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponseRedirect(reverse('activation_successful'))
    else:
        return HttpResponseRedirect(reverse('activation_unsuccessful'))

def activation_successful(request):
    return render(request, 'user/activation_successful.html')

def activation_unsuccessful(request):
    return render(request, 'user/activation_unsuccessful.html')