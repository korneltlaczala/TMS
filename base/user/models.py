from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    class Meta:
        db_table = 'auth_user'

    COACH = 'Coach'
    PARENT = 'Parent'
    PLAYER = 'Player'
    ROLE_CHOICES = [
        (COACH, 'Coach'),
        (PARENT, 'Parent'),
        (PLAYER, 'Player'),
    ]
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=PLAYER,
        null=True,
    )

