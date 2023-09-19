from rest_framework import serializers
from financials.serializers import BenefitsSerializer
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
    def create(self, validated_data):
        
        newest_beneift_record = Benefits.objects.first()
        """
        if the latest_benefit_record is returned:   
            we set the benefit foreign key of order to the newest benefit record
        else (if returned latest_benefit_record = None): --> that means thad we does not have any records in the Beneifts table
            create a new benefit record
                -> Benefits.objects.create() will return the new created 
                   and assigns its value to instance.benefit () --> benefit obj foreign key of our order instance 
        """
        validated_data['benefit'] = newest_beneift_record if newest_beneift_record is not None else Benefits.objects.create()
        return super().create(validated_data)

    class Meta:
        model = Order
        fields = ( 'id', 'date_time', 'table', 'shift', 'total_price', 'is_active', 'customer', )


class OrderItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderItem
        fields = '__all__'


class LastActiveOrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = '__all__'