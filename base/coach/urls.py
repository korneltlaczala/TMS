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
    path('choose_team/', views.choose_team, name='choose_team'),
    path('', views.dashboard, name='dashboard_coach'),
    path('players/', views.players, name='players'),
    path('player/<int:player_id>', views.player, name='player'),
    path('create_player/', views.create_player, name='create_player'),
    path('delete_player/<int:player_id>', views.delete_player, name='delete_player'),
    path('update_player/<int:player_id>', views.update_player, name='update_player'),
    path('set_team/<int:team_id>', views.set_team, name='set_team'),
    path('training_sessions/', views.training_sessions, name='training_sessions'),
    path('create_team/', views.create_team, name='create_team'),
    path('create_session/', views.create_session, name='create_session'),
]
