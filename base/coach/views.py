from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from user.models import User

# Create your views here.
from .models import Player, Team
from .forms import PlayerForm, SessionForm, TeamForm

@login_required(login_url='login')
def dashboard(request):
    team = request.user.current_team
    name = team.name.capitalize()
    player_count = Player.objects.filter(team=team).count()
    context = {
        'team': team,
        'name': name,
        'player_count': player_count
    }
    return render(request, 'coach/dashboard.html', context)

def players(request):
    current_team = request.user.current_team
    players = Player.objects.filter(team=current_team)
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
            player = form.save(commit=False)
            player.team = request.user.current_team
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
    teams = request.user.team_set.all()
    context = {'teams': teams}
    return render(request, 'coach/choose_team.html', context)

def set_team(request, team_id):
    team = Team.objects.get(id=team_id)
    request.user.current_team = team
    request.user.save()
    return HttpResponseRedirect(reverse('dashboard'))

def training_sessions(request):
    sessions = request.user.current_team.session_set.all()
    print(sessions)
    context = {sessions: sessions}
    return render(request, 'coach/training_sessions.html', context)

def create_team(request):
    coach = request.user

    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save(commit=False)
            team.coach = coach
            form.save()
            return HttpResponseRedirect(reverse('choose_team'))

    form = TeamForm()
    context = {
        'form': form,
    }

    return render(request, 'coach/team_form.html', context)

def create_session(request):
    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            session.team = request.user.current_team
            form.save()
            return HttpResponseRedirect(reverse('training_sessions'))

    form = SessionForm()
    context = {
        'form': form,
    }

    return render(request, 'coach/session_form.html', context)