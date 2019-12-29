from accounts.serializer import UserSerializer
from django.contrib.auth.models import User
from rest_framework import generics



class Register(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
 
    def perform_create(self, serializer_class):
        serializer_class.save()