from django.shortcuts import render, redirect

# Create your views here.
from .models import Player
from .forms import PlayerForm

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

def create_player(request):

    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/coach/players')

    form = PlayerForm()
    context = {
        'form': form
    }

    return render(request, 'coach/player_details.html', context)

def delete_player(request, player_id):
    player = Player.objects.get(id=player_id)
    player.delete()
    return redirect('/coach/players')

def update_player(request, player_id):
    player = Player.objects.get(id=player_id)
    if request.method == 'POST':
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return redirect('/coach/players')

    form = PlayerForm(instance=player)
    context = {
        'form': form
    }

    return render(request, 'coach/player_details.html', context)