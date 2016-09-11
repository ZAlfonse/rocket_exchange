from django.contrib import admin

from .models import Item, Rarity, Category


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'rarity')
    fields = ('name', 'category', 'rarity', ('xbox_only', 'pc_only', 'psn_only'))

admin.site.register(Rarity)
admin.site.register(Category)
