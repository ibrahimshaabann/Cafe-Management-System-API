from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField("الصنف", max_length=150,blank=True)
    price = models.DecimalField("السعر", decimal_places=2, max_digits=5)
    quantity = models.IntegerField(verbose_name="الكميه",null=True,blank=True)
    available = models.BooleanField(default=True,verbose_name="متاح")
    category = models.CharField(max_length=100,null=True,verbose_name="فئة")
    class Meta:
        verbose_name_plural = "المنيو"


    def __str__(self) :
          return f"{self.name} "