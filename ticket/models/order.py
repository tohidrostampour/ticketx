from django.db import models

from ticket.validators import validate_price, validate_count


class Order(models.Model):
    class State(models.IntegerChoices):
        WAITING = 0, 'Waiting'
        CANCELED = 1, 'Canceled'
        COMPLETED = 2, 'Completed'

    customer = models.ForeignKey(
        'customer.Customer',
        on_delete=models.CASCADE,
        related_name='orders'
    )
    ticket = models.ForeignKey(
        'ticket.Ticket',
        on_delete=models.CASCADE,
        related_name='order'
    )
    date = models.DateTimeField(
        auto_now_add=True,
    )
    count = models.IntegerField(
        validators=[validate_count],
        null=True,
        blank=True
    )
    cost = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        default=0
    )
    state = models.IntegerField(
        choices=State.choices,
        default=State.WAITING,
    )

    @property
    def orders_history(self):
        orders = self.customer.orders
        return orders.all()

    def __str__(self):
        return f'{self.customer.first_name} - {self.state}'
