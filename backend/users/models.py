from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model


class CustomUser(AbstractUser):
    pass


User = get_user_model()


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account = models.ForeignKey("Account", null=True, on_delete=models.DO_NOTHING)

    # plan = models.IntegerField(null=True)

    def __str__(self):
        if self.user.first_name and self.user.last_name:
            return f'{self.user.first_name} {self.user.last_name}'
        else:
            return self.user.username


class ThumbnailSize(models.Model):
    name = models.CharField(max_length=200)
    size = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Account(models.Model):
    name = models.CharField(max_length=200)
    thumbnail_sizes = models.ManyToManyField("ThumbnailSize", related_name='thumbnail_sizes')

    def __str__(self):
        return self.name
