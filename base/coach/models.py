import datetime
from django.db import models

from user.models import User

# Create your models here.

class Team(models.Model):

    name = models.CharField(max_length=200, null=True)
    coach = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    logo = models.ImageField(upload_to='', default='/team_badge.png', null=True, blank=True)
    
    def __str__(self):
        return f"{self.name}"

class Player(models.Model):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    name = models.CharField(max_length=200, null=True)
    surname = models.CharField(max_length=200, null=True)
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=200, null=True, choices=GENDER_CHOICES)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
    
    @property
    def age(self):
        today = datetime.date.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))

    def __str__(self):
        return f"{self.name} {self.surname} ({self.age})"

class Session(models.Model):

    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)

    players = models.ManyToManyField(Player)

    def __str__(self):
        return f"{self.date} {self.time}"