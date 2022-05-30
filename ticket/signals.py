from django.db.models.signals import post_save
from django.dispatch import receiver
from payment.models import Wallet
from ticket.models import Order
from ticket.services import complete_order


@receiver(post_save, sender=Wallet)
def process_orders(sender, instance: Wallet, created, **kwargs):
    if not created:
        user = instance.user
        orders = user.customer.orders.filter(state=Order.State.WAITING)
        initial_amount = instance.amount

        for order in orders:
            if instance.amount >= order.cost:
                complete_order(order, instance.amount)
                instance.amount -= order.cost
            else:
                break

        if initial_amount > instance.amount:
            instance.save()

