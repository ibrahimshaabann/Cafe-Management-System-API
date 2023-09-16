import django_filters
from .models import Costs

class CostsFilter(django_filters.FilterSet):
    day = django_filters.DateFilter(field_name='date', lookup_expr='day')

    class Meta:
        model = Costs
        fields= ['date']