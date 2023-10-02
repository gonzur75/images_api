from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import get_user_model



class CustomUser(AbstractUser):
    pass


User = get_user_model()

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # plan = models.ForeignKey(Plan, on_delete=models.DO_NOTHING)
    plan = models.IntegerField(null=True)