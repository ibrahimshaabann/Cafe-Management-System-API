from django.contrib import admin
from .models import Costs,Benefits

@admin.register(Costs)
class CostsAdmin(admin.ModelAdmin):
    list_display = ('id','description', 'price', 'date', 'user')

@admin.register(Benefits)
class BenefitsAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_date', 'end_date', 'benefit', 'benefit_costs', 'net_profit')

