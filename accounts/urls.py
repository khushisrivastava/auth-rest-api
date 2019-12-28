from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'api/users', views.Register.as_view(), name='Register'),
]
