from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models


class CustomUserDashboard(UserAdmin):
    list_display = ('id', 'username')
    list_editable = ('username',)
    list_display_links = ('id',)
    ordering = ('-id',)


admin.site.register(models.CustomUser, CustomUserDashboard)
