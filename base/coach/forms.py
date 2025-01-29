from django import forms
from django.forms import ModelForm
from .models import Player, Session, Team

class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = '__all__'
        exclude = ['team']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }
        
class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = '__all__'
        exclude = ['coach']

class SessionForm(ModelForm):
    class Meta:
        model = Session
        fields = '__all__'
        exclude = ['team', 'players']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }