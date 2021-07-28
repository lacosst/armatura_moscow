from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'fio', 'phone_number', 'email', 'status', 'paid', 'created', 'updated']
    list_filter = ['status', 'paid', 'created', 'updated']
    list_display_links = ['id', 'fio']
    list_editable = ['status', 'paid',]
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
