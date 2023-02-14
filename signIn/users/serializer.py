from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth import get_user_model

class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('pk','username','email')

class CreateUserSerializer(serializers.ModelSerializer):
    
    def validate_password(self, value):
        return make_password(value)
    class Meta:
        model = get_user_model()
        fields = ('id','first_name','last_name','email','password','username')
        validators = [
            UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=['email'],
                message='this user already exists'
            )
        ]
