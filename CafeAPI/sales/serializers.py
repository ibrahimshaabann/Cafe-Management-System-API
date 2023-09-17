from rest_framework import serializers
from .models import Menu,Table,Category,Order,OrderItem

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class TableSerializer(serializers.ModelSerializer):

    class Meta:
        model = Table
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'



class OrderItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderItem
        fields = '__all__'


class LastActiveOrderSerializer(serializers.ModelSerializer):
    OrderItem = OrderItemSerializer(many=True
                                    )
    class Meta:
        model = Order
        # fields = ['id', 'date_time', 'total_price','table']
        fields = '__all__'