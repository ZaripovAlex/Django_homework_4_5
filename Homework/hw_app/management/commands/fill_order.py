import datetime
import random

from django.core.management.base import BaseCommand
from hw_app.models import Items, Client, Order


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        summ = 0
        item_list = []

        for i in range(1, 6):
            for _ in range(6):
                pk = random.randint(1, 21)
                item: Items = Items.objects.filter(pk=pk).first()
                print(item)
                item_list.append(item)
                summ += int(item.price)
            print(item_list)
            print(summ)
            client = Client.objects.filter(pk=i).first()
            order = Order(
                client=client,
                # items=item_list,
                total=summ,
                date=datetime.date(2011, 1, 1)
            )
            summ = 0
            order.save()
            for item in item_list:
                order.items.add(item)
            self.stdout.write('OK')

        # order.total = sum
        # date = datetime.date(2000, 1, 1)
        # self.stdout.write('OK')
        # order.save()
