from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(r'users/', include('accounts.urls')),
]