from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .models import Offer, Listing, User


class OfferInline(admin.TabularInline):
    model = Offer


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('seller', 'created')
    fields = ('status', 'items')

    inlines = [
        OfferInline
    ]

    def save_model(self, request, obj, form, change):
        obj.seller = request.user
        obj.save()


@admin.register(User)
class UserAdmin(UserAdmin):
    pass
