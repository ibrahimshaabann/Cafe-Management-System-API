from django.shortcuts import render
from rest_framework.response import Response
from .models import Menu, OrderItem,Table,Category,Order
from .serializers import MenuSerializer,TableSerializer,CategorySerializer,OrderSerializer,OrderItemSerializer,LastActiveOrderSerializer
from .permissions import IsOwnerOrAdmin,IsAdminDelete
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication
from rest_framework import filters
from rest_framework.permissions import BasePermission
from rest_framework.decorators import api_view


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


@api_view(['GET'])
def last_active_orders(request):
    """
    API endpoint to retrieve the last active order for each table.
    """
    tables = Table.objects.all()
    
    # List to store last active orders for each table
    last_active_orders = []

    for table in tables:
        # Get the last active order for the current table
        last_order = Order.objects.filter(table=table, is_active=True).order_by('-date_time').first()
        
        # If a last active order is found for the table
        if last_order:
            serializer = LastActiveOrderSerializer(last_order)
            
            # Append the serialized data to the list
            last_active_orders.append(serializer.data)

    # Return the list of last active orders as JSON
    return Response(last_active_orders)
