from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from accounts.models import User

class UserSerializer(serializers.ModelSerializer):
    # def create(self, validated_data):
    #     user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'],validated_data['first_name'], validated_data['last_name'])
    #     return user
    #username = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())
    phone = serializers.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    class Meta:
        model = User
        fields = ('id','first_name', 'last_name', 'username', 'phone',  'email', 'password')

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')