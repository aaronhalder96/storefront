from django.dispatch import receiver
from store.models import Order
from store.signals import order_created

@receiver(order_created)
def on_order_created(sender, **kwargs):
    print(kwargs['order'])