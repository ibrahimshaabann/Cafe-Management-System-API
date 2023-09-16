from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete,pre_delete,pre_save
from .models import Shift,Employee,SalaryDeduction
from financials.models import Benefits,Costs
from sales.models import Order
def get_shift_benefits(self):
    shift_orders = self.order_set.all()
    # Calculate the total price from orders and update benefits
    total_price = sum(order.total_price for order in shift_orders)  
    self.benefits = total_price  
    self.save()


# @receiver(pre_save)
