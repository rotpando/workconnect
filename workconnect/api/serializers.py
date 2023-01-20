from rest_framework import serializers
from api.models import User,Adver

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