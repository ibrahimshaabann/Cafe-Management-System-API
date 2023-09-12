from django.db import models
from authentication.models import User 
from django.db.models.signals import post_save, post_delete,pre_delete,pre_save
from django.dispatch import receiver

"""
This class is going to be inherited from employees and employees
Note: We set abstarct = true because it is used as a template for other models to inherit from 
rather than one that is meant to be created or saved to the database
"""
class Person(models.Model):
    fname = models.CharField(max_length=60, verbose_name='الاسم الاول')
    lname = models.CharField(max_length=60, verbose_name='الاسم الثاني')
    first_address = models.CharField(max_length=400, verbose_name = 'العنوان الأول', blank=True, null=True)
    second_address = models.CharField(max_length=400, verbose_name = ' العنوان الثاني', blank=True, null=True)
    phone_no = models.CharField(max_length=11, null=False, blank=False)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return f"{self.fname} {self.lname} "


class Shift(models.Model):
    login_time = models.DateTimeField(auto_now_add=True,verbose_name='وقت الدخول')
    logout_time = models.DateTimeField(verbose_name='وقت الخروج',null=True,blank=True)
    benefits = models.DecimalField(verbose_name='الربح',
                                    max_digits=7,
                                    decimal_places=2, 
                                    default=0.00,
                                    editable=False,
                                    blank=True)
    user = models.ForeignKey(User,
                              on_delete=models.SET_NULL,
                              null=True,
                              blank=True, 
                              verbose_name="مسئول الشيفت ")

    # def get_shift_benefits(self):
    #     shift_orders = self.order_set.all()
    #     # Calculate the total price from orders and update benefits
    #     total_price = sum(order.total_price for order in shift_orders)  
              
    #     self.benefits = total_price  
    #     self.save()

    class Meta:
        verbose_name_plural = "الشيفت"
        ordering = [-1]

   
    def __str__(self) :
        return f"{self.pk} {self.user}"
    

class Employee(Person):
    salary = models.DecimalField(verbose_name='المرتب', max_digits=7, decimal_places=2)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="اسم المستخدم")
    deductions = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="خصومات", null=True, default=0)

    class Meta:
        verbose_name_plural = "الموظف"

    def __str__(self) -> str:
        return super.__str__() 
    
    
class SalaryDeduction(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="الموظف", related_name='SalaryDeduction')
    amount = models.DecimalField(verbose_name='المبلغ', max_digits=7, decimal_places=2)
    date = models.DateField(verbose_name='تاريخ الخصم', auto_now_add=True)
    description = models.CharField(max_length=255, null=True, verbose_name="سبب الخصم")

    class Meta:
        verbose_name_plural = "خصومات المرتب"
        get_latest_by = "date"

    def __str__(self):
        return f"خصم من {self.employee} بمبلغ {self.amount}"


    # def save(self, *args, **kwargs):
        
    #     super().save(*args, **kwargs)
    #     # Update the deductions field in the associated employees object
    #     total_deductions = SalaryDeduction.objects.filter(employee=self.employee).aggregate(total_deductions=models.Sum('amount'))['total_deductions']
    #     employee = self.employee
    #     employee.deductions = total_deductions if total_deductions else 0
    #     employee.save()

# @receiver(post_delete, sender=SalaryDeduction)
# def update_salary_deductions(sender, instance, **kwargs):

# # Update the deductions field in the associated Employees object

#     employee = instance.employee
#     total_deductions = SalaryDeduction.objects.filter(employee=employee).aggregate(total_deductions=models.Sum('amount'))['total_deductions']
#     employee.deductions = total_deductions if total_deductions else 0
#     employee.save()

class Attendence(models.Model):
    employee_attended = models.ForeignKey(Employee, on_delete=models.CASCADE,null=True, verbose_name='الموظف',)
    in_time = models.DateTimeField(auto_now_add=True,verbose_name='وقت الدخول', null=True, blank=True)
    out_time = models.DateTimeField(verbose_name='وقت الخروج', null=True, blank=True)
    user_created_the_attendence =  models.ForeignKey(User, on_delete=models.SET_NULL,null=True,verbose_name= "المسئول")
   
    class Meta:
            verbose_name_plural = "الحضور والانصراف"

    def __str__(self) :
        return f" {self.employee_attended} {self.login_time}{self.logout_time}User: {self.user_created_the_attendence}"
    

class Customer(Person):
    def __str__(self) -> str:
        return  super().__str__()