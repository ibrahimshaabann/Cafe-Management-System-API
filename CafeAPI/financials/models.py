from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Benefits(models.Model):
    start_date = models.DateTimeField(verbose_name="تاريخ البدايه", auto_now_add=True)
    end_date = models.DateTimeField(verbose_name="تاريخ االانتهاء", auto_now_add=True)
    benefit = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="الربح", default=0.00)
    benefit_costs = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="مصاريف الفتره", default=0.00)
    net_profit = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="صافي الربح", default=0.00)

    # def update_costs(self):
    #     # Calculate the sum of 'price' for all related Costs records
    #     total_costs = Costs.objects.filter(benefit_id=self.id).aggregate(total=Sum('price'))['total']

    #     # Update the 'costs' field in this Benefits instance
    #     self.benefit_costs = total_costs if total_costs is not None else 0.00
    #     self.net_profit = self.benefit - self.benefit_costs
    #     self.save()

    def __str__(self) :
        return f"{self.id}"

    class Meta:
        verbose_name_plural = "الأرباح"


class Costs(models.Model):
    description = models.CharField(verbose_name= 'الوصف', max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateTimeField(verbose_name="وقت الدفع", auto_now_add=True)
    user = models.ForeignKey(User, verbose_name='مسئول الشيفت', on_delete=models.SET_NULL, null=True)
    benefit_id = models.ForeignKey(Benefits, on_delete=models.SET_NULL, null=True)
    
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     if not self.benefit_id:
    #         self.benefit_id = Benefits.objects.filter().order_by('-id').first()
    #         self.benefit_id.end_date =self.date
    #         self.save()
            
    #     if self.benefit_id:
    #         self.benefit_id.end_date =self.date
    #         self.benefit_id.update_costs()

    class Meta:
        verbose_name_plural = "المصاريف"

   