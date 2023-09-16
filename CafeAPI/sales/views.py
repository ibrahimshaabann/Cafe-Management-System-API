from django.shortcuts import render
from .models import Menu, OrderItem,Table,Category,Order
from .serializers import MenuSerializer,TableSerializer,CategorySerializer,OrderSerializer,OrderItemSerializer
from .permissions import IsOwnerOrAdmin,IsAdminDelete
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication
from rest_framework import filters
from rest_framework.permissions import BasePermission
import datetime

class MenuApiView(ModelViewSet):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsOwnerOrAdmin]
    filter_backends = (DjangoFilterBackend,filters.SearchFilter, filters.OrderingFilter)
    ordering_fields = ['category']
    search_fields = ['name']



class TableApiView(ModelViewSet):
    serializer_class = TableSerializer
    queryset = Table.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsOwnerOrAdmin]
    filter_backends = (DjangoFilterBackend,filters.SearchFilter, filters.OrderingFilter)
    ordering_fields = ['id']
    search_fields = ['name']

class CategoryApiView(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsOwnerOrAdmin]
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)
    # ordering_fields = ['name']
    search_fields = ['name']

class OrderApiView(ModelViewSet):
    serializer_class = OrderSerializer
    queryset  = Order.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminDelete]
    filter_backends = (DjangoFilterBackend,filters.SearchFilter, filters.OrderingFilter)
    ordering_fields = ['-id']
    search_fields = ['id']
    

class OrderItemApiView(ModelViewSet):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [BasePermission]
    filter_backends = (DjangoFilterBackend,filters.SearchFilter, filters.OrderingFilter)
    search_fields = ['order__id']