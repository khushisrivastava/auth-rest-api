from django.conf.urls import url, include
from django.urls import path
from . import views
from django.contrib.auth import views as authViews

urlpatterns = [
    # url(r'users/', views.Register.as_view(), name='Register'),
    url(r'users/login/', views.Login.as_view(),name='Login'),
    url(r'users/register/', views.Register.as_view(), name='Register'),
    url(r'users/user/', views.UserRetrieveUpdateAPIView.as_view())
]

#urlpatterns = format_suffix_patterns(urlpatterns)