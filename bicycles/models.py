from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _


class AvailableBikeManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Bike.BikeStatus.AVAILABLE)


class ActiveOrderManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Order.OrderStatus.ACTIVE)


class Bike(models.Model):
    class BikeStatus(models.TextChoices):
        AVAILABLE = 'AV', 'Available'
        RENTED = 'RE', 'Rented'
        UNDER_RENOVATION = 'UR', 'Under renovation'
        DELETED = 'DE', 'Deleted'

    brand = models.CharField(max_length=100, verbose_name=_("bike brand"))
    model = models.CharField(max_length=100, verbose_name=_("bike model"))
    year_manufacture = models.IntegerField(verbose_name=_("year of manufacture"))
    bike_status = models.CharField(choices=BikeStatus, max_length=2, default=BikeStatus.AVAILABLE,
                                   verbose_name=_("Bike status", ))

    objects = models.Manager()
    available = AvailableBikeManager()

    class Meta:
        ordering = ['bike_status', ]
        verbose_name = 'Bike'
        verbose_name_plural = 'Bikes'

    def __str__(self):
        return f"{self.brand} {self.model} {self.year_manufacture} year"

    def get_absolute_url(self):
        pass


class Order(models.Model):
    class OrderStatus(models.IntegerChoices):
        ACTIVE = 1, "Status active"
        INACTIVE = 0, "Status inactive"

    id = models.UUIDField(primary_key=True, default=uuid.UUID, editable=False)
    order_user = models.OneToOneField(get_user_model(), models.DO_NOTHING, related_name='order',
                                      verbose_name=_("Order user"))
    bike_id = models.OneToOneField(Bike, on_delete=models.CASCADE, related_name="order", verbose_name=_("Bike"))
    order_status = models.IntegerField(choices=OrderStatus, default=OrderStatus.ACTIVE, verbose_name=_("Order status"))
    time_start = models.DateTimeField(auto_now_add=True, verbose_name=_("time start"))
    time_rent = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(169)],
                                    verbose_name=_("Time rent"))
    price_hour = models.IntegerField(verbose_name=_("Price hour"))
    total_price = models.IntegerField(verbose_name=_("Total price"))

    objects = models.Manager()
    active = ActiveOrderManager()

    class Meta:
        ordering = ['order_status']
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f"bike: {self.bike_id.name} for {self.order_user}"

    def get_absolute_url(self):
        pass
