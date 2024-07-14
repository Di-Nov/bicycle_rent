from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import CustomUser
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
