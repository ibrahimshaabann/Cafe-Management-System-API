from django.db.models.signals import pre_save, post_save,post_delete,pre_delete
from django.dispatch import receiver
from .models import Costs, Benefits
from sales.models import Order
from django.db.models import Sum,DecimalField

@receiver(pre_save, sender=Costs)
def set_benefit(sender, instance, **kwargs):
    if not instance.benefit:
        latest_benefit = Benefits.objects.order_by('-id').first()
        if latest_benefit:
            instance.benefit = latest_benefit


@receiver(post_save, sender=Costs)
def update_costs(sender, instance, **kwargs):
    # Calculate the sum of 'price' for all related Costs records
    total_costs = Costs.objects.filter(benefit=instance.benefit).aggregate(total=Sum('price'))['total']

    # Update the 'costs' field in the associated Benefits instance
    instance.benefit.benefit_costs = total_costs if total_costs is not None else 0.00
    instance.benefit.net_profit = instance.benefit.benefit - instance.benefit.benefit_costs
    instance.benefit.save()

@receiver(pre_save, sender= Order)
def set_order_benefitobj_to_last_benefit(sender, instance, **kwargs):
        latest_benefit_record = Benefits.objects.first() 
        """
        else (if returned latest_benefit_record = None): --> that means thad we does not have any records in the Beneifts table
            create a new benefit record
                -> Benefits.objects.create() will return the new created 
                   and assigns its value to instance.benefit () --> benefit obj foreign key of our order instance 
        """
        instance.benefit = latest_benefit_record if latest_benefit_record is not None else Benefits.objects.create()
        instance.benefit.save()


@receiver(post_save, sender= Order)
def update_benefit_record_benefits(sender, instance, **kwargs):
        total_orders_profit = Order.objects.filter(benefit=instance.benefit).aggregate(total=Sum('total_price'))['total'] 
        benefit_record_to_be_updated = instance.benefit
        benefit_record_to_be_updated.benefit = total_orders_profit if total_orders_profit is not None else 0.00
        benefit_record_to_be_updated.net_profit = instance.benefit.benefit - instance.benefit.benefit_costs
        benefit_record_to_be_updated.save()


@receiver(post_delete,sender = Costs)
def update__benefits_costs(sender,instance, **kwargs):
# Calculate the sum of 'price' for all related Costs records
    total_costs = Costs.objects.filter(benefit=instance.benefit).aggregate(total=Sum('price'))['total']

    # Update the 'costs' field in the associated Benefits instance
    instance.benefit.benefit_costs = total_costs if total_costs is not None else 0.00
    instance.benefit.net_profit = instance.benefit.benefit - instance.benefit.benefit_costs
    instance.benefit.save()




