from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url('api/users', views.Register),
]

urlpatterns = format_suffix_patterns(urlpatterns)