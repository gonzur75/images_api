from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models
from .models import Customer, Account, ThumbnailSize


class CustomerInline(admin.StackedInline):
    model = Customer
    can_delete = False


class AccountAdminConfig(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("name",)


class AccountInline(admin.StackedInline):
    model = Account
    can_delete = False


class ThumbnailSizeAdminConfig(admin.ModelAdmin):
    search_fields = ("name", "size")
    list_filter = ("name",)


class CustomUserDashboard(UserAdmin):
    inlines = [CustomerInline]
    list_display = ('id', 'username')
    list_editable = ('username',)
    list_display_links = ('id',)
    ordering = ('-id',)


admin.site.register(models.CustomUser, CustomUserDashboard)
admin.site.register(models.Account, AccountAdminConfig)
admin.site.register(models.ThumbnailSize, ThumbnailSizeAdminConfig)
