from accounts.serializer import UserSerializer, LoginSerializer
from rest_framework import generics
from rest_framework.authtoken.models import Token
#from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse, HttpResponse
#from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
#from django.contrib.auth import authenticate
#from django.views.decorators.csrf import csrf_exempt
from accounts.models import User
#from django.forms.models import model_to_dict



class Register(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class Login(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        data = request.data
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return JsonResponse(user, status=status.HTTP_202_ACCEPTED)
            return JsonResponse(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)



# @csrf_exempt
# @api_view(["POST"])
# @permission_classes((AllowAny,))
# def login(request):
#     username = request.data.get("username")
#     password = request.data.get("password")
#     if username is None or password is None:
#         return Response(request.data, status=status.HTTP_400_BAD_REQUEST)
#     user = authenticate(username=username, password=password)
#     if not user:
#         return Response(request.data, status=status.HTTP_404_NOT_FOUND)
#     token = Token.objects.get_or_create(user=user)
#     return Response(request.data,status=status.HTTP_200_OK)