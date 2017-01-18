from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .models import Listing, ListingItem, User


class ListingItemInline(admin.TabularInline):
    model = ListingItem


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('seller', 'value', 'created')
    fields = ('status',)
    inlines = [
        ListingItemInline,
    ]

    def save_model(self, request, obj, form, change):
        obj.seller = request.user
        obj.save()


@admin.register(User)
class UserAdmin(UserAdmin):
    pass
