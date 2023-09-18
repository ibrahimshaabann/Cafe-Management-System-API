from rest_framework import serializers

from financials.models import Benefits
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
    # benefit = serializers.PrimaryKeyRelatedField(read_only=True, required = False)
    # def create(self, validated_data):
        # validated_data['benefit'] = Benefits.objects.first()
        # return super().create(validated_data)
    
    class Meta:
        model = Order
        fields = ('__all__')


class OrderItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderItem
        fields = '__all__'


class LastActiveOrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)
    class Meta:
        model = Order
        # fields = ['id', 'date_time', 'total_price','table']
        fields = '__all__'