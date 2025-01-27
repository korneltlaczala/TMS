from django.shortcuts import render

# Create your views here.
from .models import Player

def dashboard(request):
    return render(request, 'coach/dashboard.html')

def players(request):

    players = Player.objects.all()
    context = {
        'players': players,
    }
    return render(request, 'coach/players.html', context)

def player(request, player_id):
    player = Player.objects.get(id=player_id)
    context = {
        'player': player,
    }
    return render(request, 'coach/player.html', context)