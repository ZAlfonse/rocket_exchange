from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Listing, User


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('seller', 'item', 'created', 'value')


@admin.register(User)
class UserAdmin(UserAdmin):
    pass
