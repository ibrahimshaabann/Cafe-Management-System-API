from django.contrib import admin
from .models import Menu,Order,OrderItem,Category,Table
# Register your models here.

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category','available')


admin.site.register(Table)
# admin.site.register(Order)
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_time', 'table', 'shift', 'total_price', 'is_active', 'customer')
    list_filter = ('is_active', 'date_time')
admin.site.register(OrderItem)
admin.site.register(Category)



