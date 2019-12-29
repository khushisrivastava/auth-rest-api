from django.db import models
from rest_framework.validators import UniqueValidator


class User(models.Model):
    first_name = models.CharField(blank=False, max_length=100)
    last_name = models.CharField(blank=False, max_length=100)
    # phone = models.CharField(blank=False, validators=[UniqueValidator(queryset=User.objects.all())])
    # email = models.EmailField(blank=False, validators=[UniqueValidator(queryset=User.objects.all())])
    # username = models.CharField(blank=False, validators=[UniqueValidator(queryset=User.objects.all())])
    phone = models.CharField(blank=False, max_length=10)
    email = models.EmailField(blank=False)
    username = models.CharField(blank=False, max_length=40)
    password = models.CharField(max_length=36)

