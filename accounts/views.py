from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.serializer import UserSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def Register(request, format='json'):

    if request.method == 'GET':
        serializer = UserSerializer(data={"username": "galaxyzpj", "first_name": "Pranav", "last_name": "Jain", "email": "pranav19sept@gmail.com", "password": "family19love"})
        if serializer.is_valid():
            return Response(serializer.data)

    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
