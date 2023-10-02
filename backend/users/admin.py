from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models
from .models import Customer


class CustomerInline(admin.StackedInline):
    model = Customer
    can_delete = False


class CustomUserDashboard(UserAdmin):
    inlines = [CustomerInline]
    list_display = ('id', 'username')
    list_editable = ('username',)
    list_display_links = ('id',)
    ordering = ('-id',)


admin.site.register(models.CustomUser, CustomUserDashboard)
