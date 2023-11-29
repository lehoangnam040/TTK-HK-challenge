from django.core.management.base import BaseCommand, CommandError
from order.models import Order, OrderStatus, StatusChoices, Order2, OrderStatus2


class Command(BaseCommand):
    help = "Seed data"

    def handle(self, *args, **options):
        for _ in range(20):
            order = Order.objects.create()
            status = StatusChoices.CANCELLED if order.ID % 3 == 1 else StatusChoices.COMPLETE
            OrderStatus.objects.create(
                Order=order,
                Status=status,
            )
            if order.ID % 3 == 2:
                # complete but refund
                OrderStatus.objects.create(
                    Order=order,
                    Status=StatusChoices.CANCELLED,
                )

        for _ in range(20):
            order = Order2.objects.create()
            status = StatusChoices.CANCELLED if order.ID % 3 == 1 else StatusChoices.COMPLETE
            OrderStatus2.objects.create(
                Order=order,
                Status=status,
            )
            if order.ID % 3 == 2:
                # complete but refund
                OrderStatus2.objects.create(
                    Order=order,
                    Status=StatusChoices.CANCELLED,
                )
