from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Order(models.Model):
    ID = models.BigAutoField(primary_key=True)

class StatusChoices(models.TextChoices):
    PENDING = 'PENDING', _('Pending')
    COMPLETE = 'COMPLETE', _('Complete')
    CANCELLED = 'CANCELLED', _('Cancelled')

class OrderStatus(models.Model):
    ID = models.BigAutoField(primary_key=True)
    Created = models.DateTimeField(auto_now_add=True)
    Status = models.CharField(max_length=16, choices=StatusChoices.choices, default=StatusChoices.PENDING)
    Order = models.ForeignKey(Order, models.CASCADE)


# Signals
@receiver(post_save, sender=Order, dispatch_uid="create_pending_order_status")
def create_pending_order_status(sender, instance: Order, created: bool, **kwargs):
    if created:
        OrderStatus.objects.create(
            Order=instance, Status=StatusChoices.PENDING
        )


## Optimized models
class Order2(models.Model):
    ID = models.BigAutoField(primary_key=True)
    LatestStatus = models.CharField(max_length=16, choices=StatusChoices.choices, default=StatusChoices.PENDING)
    LatestStatusAt = models.DateTimeField(auto_now_add=True)

class OrderStatus2(models.Model):
    ID = models.BigAutoField(primary_key=True)
    Created = models.DateTimeField(auto_now_add=True)
    Status = models.CharField(max_length=16, choices=StatusChoices.choices, default=StatusChoices.PENDING)
    Order = models.ForeignKey(Order2, models.CASCADE)

@receiver(post_save, sender=Order2, dispatch_uid="create_pending_order_status2")
def create_pending_order_status2(sender, instance: Order2, created: bool, **kwargs):
    if created:
        OrderStatus2.objects.create(
            Order=instance, Status=StatusChoices.PENDING, Created=instance.LatestStatusAt,
        )

@receiver(post_save, sender=OrderStatus2, dispatch_uid="update_latest_status_order2")
def update_latest_status_order2(sender, instance: OrderStatus2, created: bool, **kwargs):
    if created and instance.Status != StatusChoices.PENDING:
        Order2.objects.filter(ID=instance.Order.pk).update(
            LatestStatus=instance.Status,
            LatestStatusAt=instance.Created,
        )