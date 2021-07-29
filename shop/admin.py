from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}


class ProductAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'slug', '' 'price_toon', 'price', 'stock', 'available', 'updated']
    list_filter = ['available', 'created', 'updated', 'category']
    list_editable = ['price_toon', 'stock', 'available']
    prepopulated_fields = {'slug': ('name', 'mark_steel')}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

admin.site.site_title = 'ARMATURA.MOSCOW'
admin.site.site_header = 'ARMATURA.MOSCOW'