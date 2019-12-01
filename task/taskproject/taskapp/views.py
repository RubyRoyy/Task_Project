from django.contrib.auth.models import User
from django.shortcuts import render

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from datetime import datetime, date, timedelta
from .models import UserData
from .serializers import UserSerializer, LoginSerializer, DateSerializer, UpdateSerializer

class UserListView(APIView):

    def get(self, request):
        data = User.objects.all()
        serializer = UserSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SignUp(APIView):

    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):

    def get(self, request):
        data = request.data
        serializer = LoginSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ProfileUpdateView(APIView):

    permission_classes = [IsAuthenticated, ]
    serializer_class = UpdateSerializer

    def get(self, request, username):
        if username==str(request.user):
            try:
                user1 = User.objects.get(username=username)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = UpdateSerializer(user1)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("Not allowed")

    def put(self, request, username):
        if username == str(request.user):
            try:
                data1 = User.objects.get(username=username)
            except:
                return Response({'msg': "record not found"}, status=status.HTTP_404_NOT_FOUND)
            data = request.data
            serializer = UpdateSerializer(data1, data=data)
            if serializer.is_valid():
                serializer.save()
                data = UserData.objects.get(user=request.user)
                data.modified_on=datetime.now()
                data.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("You can only update your profile", status=status.HTTP_400_BAD_REQUEST)


class DateData(APIView):

    serializer_class = DateSerializer

    def post(self, request):
        serializer = DateSerializer(data=request.data)
        if serializer.is_valid():
            s=serializer.data['startdate']
            e = serializer.data['enddate']
            # print(type(e))
            # data=User.objects.filter(date_joined=)
            # print(data)
            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






