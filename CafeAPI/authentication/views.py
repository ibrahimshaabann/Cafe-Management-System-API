from django.conf import settings
from django.shortcuts import render
from .permissions import IsUserOwner, IsAdminOrReadOnly
from rest_framework import viewsets
from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsUserOwner | IsAdminOrReadOnly]
    # filter_backends = None

