from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UserAdmin_default
from .models import User

# Register your models here.

class UserAdmin(UserAdmin_default):
    model = User

admin.site.register(User, UserAdmin)