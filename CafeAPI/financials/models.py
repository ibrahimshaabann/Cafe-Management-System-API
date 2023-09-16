from django.db import models
from authentication.models import User


class Benefits(models.Model):
    start_date = models.DateTimeField(verbose_name="تاريخ البدايه", auto_now_add=True)
    end_date = models.DateTimeField(verbose_name="تاريخ االانتهاء", auto_now=True)
    benefit = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="الربح", default=0.00)
    benefit_costs = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="مصاريف الفتره", default=0.00)
    net_profit = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="صافي الربح", default=0.00)

    def __str__(self) :
        return f"{self.id}"

    class Meta:
        ordering = ['-id']
        verbose_name_plural = "الأرباح"


class Costs(models.Model):
    description = models.CharField(verbose_name= 'الوصف', max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateTimeField(verbose_name="وقت الدفع", auto_now_add=True)
    user = models.ForeignKey(User, verbose_name='مسئول الشيفت', on_delete=models.SET_NULL, null=True)
    benefit = models.ForeignKey(Benefits, blank=True,on_delete=models.SET_NULL, null=True)
    
    class Meta:
        ordering = ['-id']
        verbose_name_plural = "المصاريف"

   