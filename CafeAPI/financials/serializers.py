from rest_framework import serializers
from financials.models import Benefits,Costs

class BenefitsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Benefits
        fields = '__all__'  


class CostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Costs
        fields = '__all__'
