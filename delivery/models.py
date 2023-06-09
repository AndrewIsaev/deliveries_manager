from time import strptime

from django.db import models
from django.utils.datetime_safe import strftime


# Create your models here.
class Supplier(models.Model):
    """Supplier Model"""

    title = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"

    def __str__(self):
        return f"{self.title} {self.country}"


class Material(models.Model):
    """Material Model"""

    sap_number = models.PositiveIntegerField()
    description = models.CharField(max_length=250)
    supplier = models.ForeignKey("delivery.Supplier", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Материал"
        verbose_name_plural = "Материалы"

    def __str__(self):
        return f"{self.sap_number} {self.description}"


class Delivery(models.Model):
    """Delivery Model"""

    material = models.ForeignKey("delivery.Material", on_delete=models.CASCADE)
    supplier = models.ForeignKey("delivery.Supplier", on_delete=models.CASCADE)
    shipment_date = models.DateField(null=True, blank=True)
    delivery_date = models.DateField(null=True, blank=True)
    shipment_week = models.PositiveSmallIntegerField(null=True, blank=True)
    delivery_week = models.PositiveSmallIntegerField(null=True, blank=True)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.shipment_week = self.shipment_date.strftime("%W")
        self.delivery_week = self.delivery_date.strftime("%W")
        return super().save()

    class Meta:
        verbose_name = "Поставка"
        verbose_name_plural = "Поставки"

    def __str__(self):
        return f"{self.supplier.title} {self.material.sap_number}"
