from django.contrib import admin

from delivery.models import Delivery, Material, Supplier


# Register your models here.
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    pass


@admin.register(Material)
class SupplierAdmin(admin.ModelAdmin):
    pass


@admin.register(Delivery)
class SupplierAdmin(admin.ModelAdmin):
    pass
