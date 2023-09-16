from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete,pre_delete,pre_save
from .models import Shift,Employee,SalaryDeduction
from financials.models import Benefits,Costs
from sales.models import Order
from django.db.models import Sum

# def get_shift_benefits(self):
#     shift_orders = self.order_set.all()
#     # Calculate the total price from orders and update benefits
#     total_price = sum(order.total_price for order in shift_orders)  
#     self.benefits = total_price  
#     self.save()


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
