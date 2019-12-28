from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'api/users', views.Register.as_view(), name='Register'),
]

urlpatterns = format_suffix_patterns(urlpatterns)