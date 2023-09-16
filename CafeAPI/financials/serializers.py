from rest_framework import serializers
from financials.models import Benefits,Costs

class BenefitsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Benefits
        fields = '__all__'  


class CostsSerializer(serializers.ModelSerializer):
    benefit = Benefits.objects.filter(id=2).first()
    print(benefit)
    class Meta:
        model = Costs
        fields = ['description', 'price']
