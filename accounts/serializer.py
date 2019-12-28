from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    # first_name = serializers.CharField(required=True, max_length=100)
    # last_name = serializers.CharField(required=True, max_length=100)
    # #phone = serializers.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    # email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    # username = serializers.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    # password = serializers.CharField(min_length=6, write_only=True)

    # def create(self, validated_data):
    #     user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
    #     return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')#, 'phone')