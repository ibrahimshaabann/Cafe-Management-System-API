from django.db.models.signals import post_save,pre_save,pre_delete,post_delete
from django.dispatch import receiver
from .models import *
from human_resources.models import Shift

@receiver(pre_save,sender=OrderItem)
def OrderItem_pre_save(sender, instance, **kwargs):
    instance.price = instance.item.price * instance.quantity
    previous_quantity = 0

    if instance.pk:
        previous_quantity = OrderItem.objects.get(pk=instance.pk).quantity
    quantity_change = instance.quantity - previous_quantity

    if instance.item.quantity is not None:
        instance.item.quantity -= quantity_change
    instance.item.save()

@receiver(post_save,sender=OrderItem)
def update_total_Price(sender, instance, **kwargs):
    order_items = instance.order.order_items.all()
    total_price = sum(item.price for item in order_items)
    instance.order.total_price = total_price
    # print(total_price)
    instance.order.save()


@receiver(pre_delete,sender=OrderItem)
def update_item_quantity(sender,instance,**kwargs):
    if instance.item.quantity != None:
      instance.item.quantity += instance.quantity
    instance.item.save()


@receiver(post_delete, sender=OrderItem)
def update_total_price_on_delete(sender, instance, **kwargs):
    order_items = instance.order.order_items.all()
    total_price = sum(item.price for item in order_items)
    instance.order.total_price = total_price
    # print(total_price)
    instance.order.save()
 
    