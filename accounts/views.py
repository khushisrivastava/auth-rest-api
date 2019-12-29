from accounts.serializer import UserSerializer
from accounts.models import User
from rest_framework import generics



class Register(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
 

    