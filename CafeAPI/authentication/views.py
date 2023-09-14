from django.conf import settings
from django.shortcuts import render
# import jwt
from .permissions import IsAdmin, IsOwnerOrReadOnly

from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, IsAdmin]
    # filter_backends = None

