from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.validators import UniqueValidator


class User(AbstractUser):
    phone = models.CharField(blank=False, max_length=10)
    #date_of_birth = models.DateTimeField(blank=True)

