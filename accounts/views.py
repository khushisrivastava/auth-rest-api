from accounts.serializer import RegisterSerializer, LoginSerializer, UserSerializer
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from .renderers import UserJSONRenderer
from accounts.models import User

class Register(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class Login(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    # renderer_classes = (UserJSONRenderer,)
    serializer_class = UserSerializer

    def retrieve(self, request):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request):
        serializer_data = request.GET.get('user')
        serializer = self.serializer_class(
            request.data, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

# class Login(generics.RetrieveAPIView):
#     permission_classes = [AllowAny]
#     queryset = User.objects.all()
#     serializer_class = LoginSerializer
#     def post(self, request, format=None):
#         data = request.data
#         serializer = LoginSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             if user:
#                 token = Token.objects.create(user=user)
#                 json = serializer.data
#                 json['token'] = token.key
#                 return JsonResponse(user, status=status.HTTP_202_ACCEPTED)
#             return JsonResponse(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)





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