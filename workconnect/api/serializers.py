from rest_framework import serializers
from api.models import UserProfile,Adver
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class AdverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adver
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'