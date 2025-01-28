"""
URL configuration for base project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    # path('login/', views.login, name='login'),
    # path('', views.login, name='login'),
    path('', views.login, name='login'),
    path('login/', views.login2, name='login2'),
    path('logout/', views.logout, name='logout'),
    path('choose_account_type/', views.choose_account_type, name='choose_account_type'),
    path('register/<str:type>/', views.register, name='register'),
    path('register_coach/', views.register_coach, name='register_coach'),
    path('register_parent/', views.register_parent, name='register_parent'),
    path('register_player/', views.register_player, name='register_player'),
    path('password_reset/', views.password_reset, name='password_reset'),
    path('confirm_email/', views.confirm_email, name='confirm_email'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('activation_successful/', views.activation_successful, name='activation_successful'),
    path('activation_unsuccessful/', views.activation_unsuccessful, name='activation_unsuccessful'),
    path('terms/', views.terms, name='terms'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
]
