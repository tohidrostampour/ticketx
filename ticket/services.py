from rest_framework.exceptions import ValidationError
from django.db import transaction
from ticket.models import Order, Receipt


@transaction.atomic()
def complete_order(order: Order, credit: int = 0):
    ticket = order.ticket
    if order.count > ticket.count:
        order.state = Order.State.CANCELED
        order.save()
        transaction.commit()
        raise ValidationError("cannot order more than available ticket count")

    if credit < order.cost:
        raise ValidationError("not enough credit")

    ticket.count -= order.count
    ticket.save()

    receipts = []
    for i in range(order.count):
        receipts.append(Receipt(order=order))

    Receipt.objects.bulk_create(receipts)
    order.state = Order.State.COMPLETED
    order.save()
