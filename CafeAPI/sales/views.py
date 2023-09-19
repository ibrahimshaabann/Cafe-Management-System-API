from rest_framework.response import Response
from .models import Menu, OrderItem,Table,Category,Order
from .serializers import MenuSerializer,TableSerializer,CategorySerializer,OrderSerializer,OrderItemSerializer,LastActiveOrderSerializer
from .permissions import IsOwnerOrAdmin,IsAdminDelete
from rest_framework.viewsets import ModelViewSet, ViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication
from rest_framework import filters, status
from rest_framework.permissions import BasePermission



class MenuApiView(ModelViewSet):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsOwnerOrAdmin]
    filter_backends = (DjangoFilterBackend,filters.SearchFilter, filters.OrderingFilter)
    ordering_fields = ['category']
    search_fields = ['name']



class TableApiView(ModelViewSet):
    serializer_class = TableSerializer
    queryset = Table.objects.all()
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsOwnerOrAdmin]
    filter_backends = (DjangoFilterBackend,filters.SearchFilter, filters.OrderingFilter)
    ordering_fields = ['id']
    search_fields = ['name']

class CategoryApiView(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    authentication_classes = [BasicAuthentication]
    # permission_classes = [IsOwnerOrAdmin]
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)
    # ordering_fields = ['name']
    search_fields = ['name']

class OrderApiView(ModelViewSet):
    serializer_class = OrderSerializer
    queryset  = Order.objects.all()
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAdminDelete]
    filter_backends = (DjangoFilterBackend,filters.SearchFilter, filters.OrderingFilter)
    ordering_fields = ['-id']
    search_fields = ['id']
    
    

class OrderItemApiView(ModelViewSet):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [BasePermission]
    filter_backends = (DjangoFilterBackend,filters.SearchFilter, filters.OrderingFilter)
    search_fields = ['order__id']

class last_active_orders(ViewSet):
    # permission_classes = [IsAdminDelete]
    def list(self, request):
        """
        List last active orders for each table.
        """
        tables = Table.objects.all()
        last_active_orders = []
        for table in tables:
            last_order = Order.objects.filter(table=table).order_by('-date_time').first()
            if last_order:
                serializer = LastActiveOrderSerializer(last_order)
                last_active_orders.append(serializer.data)
        return Response(last_active_orders)
    def retrieve(self, request, pk=None):
        """
        Retrieve a specific order by ID.
        """
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Response({"message": "Order not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = LastActiveOrderSerializer(order)
        return Response(serializer.data)