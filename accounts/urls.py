from django.conf.urls import url, include
from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'api/users', views.Register.as_view(), name='Register'),
    url(r'api/login<int>', views.Login.as_view(),name='Login')
    
]

urlpatterns = format_suffix_patterns(urlpatterns)