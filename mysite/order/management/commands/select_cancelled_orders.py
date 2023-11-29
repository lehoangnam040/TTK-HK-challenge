from django.core.management.base import BaseCommand, CommandError
from order.models import Order, OrderStatus, StatusChoices, Order2
from django.db.models.expressions import Window, F
from django.db.models.functions import Rank

class Command(BaseCommand):
    help = "Select all cancelled orders with ORM"

    def handle(self, *args, **options):
        print("=============== USING ORM ===========")
        orders = OrderStatus.objects.annotate(rank=Window(
            expression=Rank(),
            order_by=F('Created').desc(),
            partition_by=[F('Order')]
        )).filter(
            Status=StatusChoices.CANCELLED
        ).order_by('Order').values(
            'Order', 'Created', 'Status'
        )
        for order in orders:
            print(order)
        

        print("=============== USING Optimized Models ===========")
        orders = Order2.objects.filter(
            LatestStatus=StatusChoices.CANCELLED
        ).order_by('ID').values()
        for order in orders:
            print(order)