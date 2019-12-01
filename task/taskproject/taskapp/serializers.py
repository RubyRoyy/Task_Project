from .models import UserData,DateModel
import datetime
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=('username','password','email','is_active')
        extra_kwargs = {'password': {'write_only': True}}
        # fields='__all__'

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        userdata = UserData.objects.create(
            user=user,
            modified_on=datetime.datetime.now(),
        )
        return user


class UpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=('username','email','is_active')


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('username','password')
        extra_kwargs = {'password': {'write_only': True}}


class DateSerializer(serializers.ModelSerializer):
    startdate = serializers.DateField()
    enddate = serializers.DateField()


    class Meta:
        model = DateModel
        # fields = '__all__'
        fields = ('startdate','enddate')

