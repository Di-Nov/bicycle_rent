from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import CustomUser





class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
