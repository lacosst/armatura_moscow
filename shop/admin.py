from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}


class ProductAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'mark_steel', 'meter_weight', 'price_toon', 'price',  'available', 'updated']
    list_filter = ['available', 'created', 'updated', 'category']
    list_editable = ['meter_weight', 'price_toon', 'available']
    list_display_links = ['category', 'name']
    prepopulated_fields = {'slug': ('name', 'mark_steel')}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

admin.site.site_title = 'ARMATURA.MOSCOW'
admin.site.site_header = 'ARMATURA.MOSCOW'