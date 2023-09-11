from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

class User(AbstractUser): 
    

    class Roles(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        SUPERUSER = 'superuser', 'SuperUser'
        USER = 'user', 'User'


    role = models.TextField(choices=Roles.choices,
                            default=Roles.USER,
                            null=False
                            )
    
    # @receiver(post_save, sender = settings.AUTH_USER_MODEL)
    # def create_user_token(sender, instance = None):
    #     pass

   
