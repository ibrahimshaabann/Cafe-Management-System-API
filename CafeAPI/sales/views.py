from django.shortcuts import render
from .models import Menu,Table,Category
from .serializers import MenuSerializer,TableSerializer,CategorySerializer
from .permissions import IsOwnerOrAdmin
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication
from rest_framework import filters


class MenuApiView(ModelViewSet):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsOwnerOrAdmin]
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = ['category']


class TableApiView(ModelViewSet):
    serializer_class = TableSerializer
    queryset = Table.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsOwnerOrAdmin]
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = ['id']


class CategoryApiView(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsOwnerOrAdmin]
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = ['name']


