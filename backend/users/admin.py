from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models
from .models import Account


class AccountAdminConfig(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("name",)


class ThumbnailSizeAdminConfig(admin.ModelAdmin):
    search_fields = ("id", "size")
    list_filter = ("size",)


class CustomUserDashboard(UserAdmin):
    list_display = ('id', 'username', 'account')
    list_editable = ('account',)
    list_display_links = ('id', 'username')
    ordering = ('-id',)


admin.site.register(models.CustomUser, CustomUserDashboard)
admin.site.register(models.Account, AccountAdminConfig)
admin.site.register(models.ThumbnailSize, ThumbnailSizeAdminConfig)

admin.site.site_header = 'Admin Panel'
admin.site.site_title = 'Thumbnail provider'
