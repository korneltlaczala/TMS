from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Player
from .forms import PlayerForm

@login_required(login_url='login')
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
            return redirect('players')

    form = PlayerForm()
    context = {
        'form': form
    }

    return render(request, 'coach/player_form.html', context)

def delete_player(request, player_id):
    if request.method == 'POST':
        player = Player.objects.get(id=player_id)
        player.delete()
        return redirect('players')
    
    player = Player.objects.get(id=player_id)
    context = {
        'player': player
    }
    return render(request, 'coach/delete_player.html', context)

def update_player(request, player_id):
    player = Player.objects.get(id=player_id)
    if request.method == 'POST':
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return redirect('players')

    form = PlayerForm(instance=player)
    context = {
        'form': form
    }

    return render(request, 'coach/player_form.html', context)

def choose_team(request):
    return render(request, 'coach/choose_team.html')