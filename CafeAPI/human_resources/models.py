from typing import Any, Dict, Iterable, Optional, Tuple
from django.db import models
from authentication.models import User 
from django.db.models.signals import post_save, post_delete,pre_delete,pre_save
from django.dispatch import receiver

class Shift(models.Model):
    login_time = models.DateTimeField(auto_now_add=True,verbose_name='وقت الدخول')
    logout_time = models.DateTimeField(verbose_name='وقت الخروج',null=True,blank=True)
    benefits = models.DecimalField(verbose_name='الربح',
                                    max_digits=7,
                                    decimal_places=2, 
                                    default=0.00,
                                    editable=False,
                                    blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True, verbose_name="مسئول الشيفت ")

    # def get_shift_benefits(self):
    #     shift_orders = self.order_set.all()
    #     # Calculate the total price from orders and update benefits
    #     total_price = sum(order.total_price for order in shift_orders)  
              
    #     self.benefits = total_price  
    #     self.save()

    class Meta:
        verbose_name_plural = "الشيفت"

   
    def __str__(self) :
        return f"{self.pk} {self.user}"
    

class Workers(models.Model):
    fname = models.CharField(max_length=60, verbose_name='الاسم الاول')
    lname = models.CharField(max_length=60, verbose_name='الاسم الثاني')
    salary = models.DecimalField(verbose_name='المرتب', max_digits=7, decimal_places=2)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="اسم المستخدم")
    deductions = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="خصومات", null=True, default=0)

    class Meta:
        verbose_name_plural = "الموظف"

    def __str__(self):
        return f" {self.fname} {self.lname}"
    
    
class SalaryDeduction(models.Model):
    worker = models.ForeignKey(Workers, on_delete=models.CASCADE, verbose_name="الموظف", related_name='SalaryDeduction')
    amount = models.DecimalField(verbose_name='المبلغ', max_digits=7, decimal_places=2)
    date = models.DateField(verbose_name='تاريخ الخصم', auto_now_add=True)
    description = models.CharField(max_length=255, null=True, verbose_name="سبب الخصم")

    class Meta:
        verbose_name_plural = "خصومات المرتب"

    def __str__(self):
        return f"خصم من {self.worker} بمبلغ {self.amount}"


    # def save(self, *args, **kwargs):
        
    #     super().save(*args, **kwargs)
    #     # Update the deductions field in the associated Workers object
    #     total_deductions = SalaryDeduction.objects.filter(worker=self.worker).aggregate(total_deductions=models.Sum('amount'))['total_deductions']
    #     worker = self.worker
    #     worker.deductions = total_deductions if total_deductions else 0
    #     worker.save()



# @receiver(post_delete, sender=SalaryDeduction)
# def update_salary_deductions(sender, instance, **kwargs):

# # Update the deductions field in the associated Workers object

#     worker = instance.worker
#     total_deductions = SalaryDeduction.objects.filter(worker=worker).aggregate(total_deductions=models.Sum('amount'))['total_deductions']
#     worker.deductions = total_deductions if total_deductions else 0
#     worker.save()

class Attendence(models.Model):
    worker_attended = models.ForeignKey(Workers, on_delete=models.CASCADE,null=True, verbose_name='الموظف',)
    login_time = models.DateTimeField(auto_now_add=True,verbose_name='وقت الدخول', null=True, blank=True)
    logout_time = models.DateTimeField(verbose_name='وقت الخروج', null=True, blank=True)
    user_created_the_attendence =  models.ForeignKey(User, on_delete=models.SET_NULL,null=True,verbose_name= "المسئول")
   
    class Meta:
            verbose_name_plural = "الحضور والانصراف"

    def __str__(self) :
        return f" {self.worker_attended} {self.login_time}{self.logout_time}User: {self.user_created_the_attendence}"