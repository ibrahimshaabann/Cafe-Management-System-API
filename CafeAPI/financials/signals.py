from django.db.models.signals import post_save,pre_save,pre_delete,post_delete
from django.dispatch import receiver
from .models import Costs,Benefits

