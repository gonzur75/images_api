from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model


class CustomUser(AbstractUser):
    account = models.ForeignKey("Account", null=True, on_delete=models.SET_NULL, related_name='account')


class Account(models.Model):
    name = models.CharField(max_length=200)
    thumbnail_sizes = models.ManyToManyField("ThumbnailSize", related_name='thumbnail_sizes')
    has_link = models.BooleanField(default=False)
    has_expiring_link = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ThumbnailSize(models.Model):
    size = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.size}px'
