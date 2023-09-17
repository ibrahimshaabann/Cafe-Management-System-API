from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Costs, Benefits
from django.db.models import Sum

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
