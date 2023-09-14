from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from .models import *

@receiver(pre_save,sender=OrderItem)
def OrderItem_post_save(sender,instance,**kwargs):
    instance.price = instance.item.price * instance.quantity