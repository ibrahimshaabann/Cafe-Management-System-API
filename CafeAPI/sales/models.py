from django.db import models
from human_resources.models import Customer,Shift
# Create your models here.


class Table(models.Model):
    name = models.CharField(max_length=150, verbose_name="اسم الطاوله",null=True)

    class Meta:
        verbose_name_plural = "الطاولة"

    def __str__(self):
        return f" {self.name}"

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم الفئة")
    description = models.TextField(blank=True, verbose_name="وصف الفئة")

    class Meta:
        verbose_name_plural = "الفئات"

    def __str__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField("الصنف", max_length=150)
    price = models.DecimalField("السعر", decimal_places=2, max_digits=5)
    quantity = models.IntegerField(verbose_name="الكميه",null=True,blank=True)
    available = models.BooleanField(default=True,verbose_name="متاح")
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,verbose_name="فئة")
    class Meta:
        verbose_name_plural = "المنيو"


    def __str__(self) :
          return f"{self.name} "
    


class Order(models.Model):
    date_time = models.DateTimeField("وقت الاوردر", auto_now=True)
    table = models.ForeignKey(Table, null=True, on_delete=models.SET_NULL, verbose_name="طاولة")
    shift = models.ForeignKey(Shift,related_name='order_set', null=True, on_delete=models.SET_NULL, verbose_name="شيفت")
    total_price = models.DecimalField("اجمالي السعر", max_digits=7, decimal_places=2, default=0.00)
    is_active = models.BooleanField(verbose_name="نشط",default=True)
    # benefit_id = models.ForeignKey(Benefits, on_delete=models.SET_NULL, null=True, verbose_name="رقم فتره الربح")
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True,verbose_name="العميل")
    class Meta:
        verbose_name_plural = "الاوردرات"
        ordering = ['-date_time']
        ordering = ['-id']
    def __str__(self):
        return f"{self.pk}"
    


class OrderItem(models.Model):
    order = models.ForeignKey(Order,related_name='order_items', on_delete = models.CASCADE ,verbose_name="اوردر")
    item = models.ForeignKey(Menu, null=True,on_delete=models.DO_NOTHING,verbose_name="الصنف")
    quantity = models.IntegerField("كميه")
    price = models.DecimalField(verbose_name="سعر", max_digits=5, decimal_places=2, default=0.00)

    class Meta:
        verbose_name_plural = "عنصر الاوردر"

    def __str__(self):
        return f"{self.quantity} {self.item.name}"


class active_order(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    table = models.ForeignKey(Table,on_delete=models.CASCADE)