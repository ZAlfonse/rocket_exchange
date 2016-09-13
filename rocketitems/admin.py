from django.contrib import admin

from .models import Item, Quality, Type, Pack, Attribute, Variation, VariationAttribute


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'quality')
    fields = ('name', 'type', 'quality', 'pack', ('xbox_only', 'pc_only', 'psn_only'))


class VariationAttributeInline(admin.TabularInline):
    model = VariationAttribute


@admin.register(Variation)
class Variation(admin.ModelAdmin):
    inlines = [
        VariationAttributeInline
    ]

admin.site.register(Quality)
admin.site.register(Type)
admin.site.register(Pack)
admin.site.register(Attribute)
