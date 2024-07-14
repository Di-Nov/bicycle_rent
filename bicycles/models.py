from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


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

    brand = models.CharField(max_length=100, verbose_name="bike brand")
    model = models.CharField(max_length=100, verbose_name="bike brand")
    year_manufacture = models.IntegerField(verbose_name="year of manufacture")
    bike_status = models.CharField(choices=BikeStatus, max_length=2, default=BikeStatus.AVAILABLE,
                                   verbose_name="Bike status", )

    class Meta:
        ordering = ['bike_status', ]
        verbose_name = 'Bike'
        verbose_name_plural = 'Bikes'

    def __str__(self):
        return f"{Bike.brand} {Bike.model} {Bike.year_manufacture} year"

    def get_absolute_url(self):
        pass


class Order(models.Model):
    class OrderStatus(models.IntegerChoices):
        ACTIVE = 1, "Status active"
        INACTIVE = 0, "Status inactive"

    id = models.IntegerField(primary_key=True)
    order_user = models.OneToOneField(get_user_model(), models.DO_NOTHING, related_name='order',
                                      verbose_name="Order user")
    bike_id = models.OneToOneField(Bike, on_delete=models.CASCADE, related_name="order", verbose_name="Bike")
    order_status = models.IntegerField(choices=OrderStatus, default=OrderStatus.ACTIVE, verbose_name="Order status")
    time_start = models.DateTimeField(auto_now_add=True, verbose_name="time start")
    time_rent = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(169)], verbose_name="Time rent")
    price_hour = models.IntegerField(verbose_name="Price hour")
    total_price = models.IntegerField(verbose_name="Total price")

    class Meta:
        ordering = ['order_status']
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f"Order number {Order.id}, bike: {Order.bike_id.name} for {Order.order_user.name}"

    def get_absolute_url(self):
        pass
