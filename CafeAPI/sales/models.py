from django.db import models

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
    name = models.CharField("الصنف", max_length=150,blank=True)
    price = models.DecimalField("السعر", decimal_places=2, max_digits=5)
    quantity = models.IntegerField(verbose_name="الكميه",null=True,blank=True)
    available = models.BooleanField(default=True,verbose_name="متاح")
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,verbose_name="فئة")
    class Meta:
        verbose_name_plural = "المنيو"


    def __str__(self) :
          return f"{self.name} "
    


    


