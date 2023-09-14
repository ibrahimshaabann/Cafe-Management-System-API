from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Costs, Benefits
from django.db.models import Sum

@receiver(pre_save, sender=Costs)
def set_benefit_id(sender, instance, **kwargs):
    if not instance.benefit_id:
        latest_benefit = Benefits.objects.order_by('-id').first()
        if latest_benefit:
            instance.benefit_id = latest_benefit
            instance.benefit_id.end_date = instance.date

@receiver(post_save, sender=Costs)
def update_benefit_costs(sender, instance, **kwargs):
    if instance.benefit_id:
        benefit = Benefits.objects.get(pk=instance.benefit_id)
        benefit.end_date = instance.date
        benefit.save()

@receiver(post_save, sender=Costs)
def update_costs(sender, instance, **kwargs):
    # Calculate the sum of 'price' for all related Costs records
    total_costs = Costs.objects.filter(benefit_id=instance.benefit_id).aggregate(total=Sum('price'))['total']

    # Update the 'costs' field in the associated Benefits instance
    instance.benefit.benefit_costs = total_costs if total_costs is not None else 0.00
    instance.benefit.net_profit = instance.benefit.benefit - instance.benefit.benefit_costs
    instance.benefit.save()
