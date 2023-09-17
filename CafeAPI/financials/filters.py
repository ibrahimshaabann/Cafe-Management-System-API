import django_filters
from .models import Costs

class CostsFilter(django_filters.FilterSet):
    # field_name refers to the attribute in the model
    price_in_URL = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    date_in_URL = django_filters.DateTimeFilter(field_name='date', lookup_expr='month')

    class Meta:
        model = Costs
        fields = ['price_in_URL', 'date_in_URL']