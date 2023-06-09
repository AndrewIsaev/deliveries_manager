from django.contrib import admin

from delivery.models import Delivery, Material, Supplier


# Register your models here.
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['title', 'country']


@admin.register(Material)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['sap_number', 'description', 'supplier']


@admin.register(Delivery)
class SupplierAdmin(admin.ModelAdmin):
    list_display = [
        'material',
        'supplier',
        'shipment_date',
        'delivery_date',
        'shipment_week',
        'delivery_week',
    ]
