from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete,pre_delete,pre_save
from .models import Shift,Employee,SalaryDeduction
from financials.models import Benefits,Costs
from sales.models import Order
from django.db.models import Sum

@receiver(post_save, sender = SalaryDeduction)
def update_employee_salary(sender, instance, **kwargs):
    total_deductions = SalaryDeduction.objects.filter(employee=instance.employee).aggregate(total_deductions=Sum('amount'))['total_deductions']
    employee = instance.employee 
    employee.deductions = total_deductions if total_deductions else 0
    employee.save()

@receiver(post_delete, sender=SalaryDeduction)
def update_salary_deductions(sender, instance, **kwargs):

# Update the deductions field in the associated Employees object
    employee = instance.employee
    total_deductions = SalaryDeduction.objects.filter(employee=employee).aggregate(total_deductions=Sum('amount'))['total_deductions']
    employee.deductions = total_deductions if total_deductions else 0
    employee.save()

@receiver(post_save ,sender = Order)
def get_shift_benefits(sender, instance, **kwargs):
    shift_obj = instance.shift
    shift_orders = shift_obj.order_set.all()
    total_price = sum(order.total_price for order in shift_orders)  
    shift_obj.benefits = total_price  
    shift_obj.save()


@receiver(post_delete ,sender = Order)
def get_shift_benefits(sender, instance, **kwargs):
    shift_obj = instance.shift
    shift_orders = shift_obj.order_set.all()
    total_price = sum(order.total_price for order in shift_orders)  
    shift_obj.benefits = total_price  
    shift_obj.save()

