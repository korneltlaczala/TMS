# Generated by Django 5.1.5 on 2025-01-29 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coach', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
