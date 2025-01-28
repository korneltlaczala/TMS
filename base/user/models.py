from functools import cached_property
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# class MyUser(AbstractUser):
#     email_confirmed = models.BooleanField(default=False)
#     confirmation_token = models.CharField(max_length=200, null=True, blank=True)
#     token_created_at = models.DateTimeField(null=True, blank=True)
