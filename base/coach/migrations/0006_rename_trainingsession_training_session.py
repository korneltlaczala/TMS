# Generated by Django 5.1.5 on 2025-01-29 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coach', '0005_alter_player_team_alter_team_coach_trainingsession'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TrainingSession',
            new_name='Training_session',
        ),
    ]
