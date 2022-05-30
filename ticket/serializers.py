from rest_framework.serializers import ModelSerializer

from ticket.models import Ticket, Order, Receipt
from customer.serializers import CustomerSerializer


class TicketSerializer(ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'
        read_only_fields = ('user',)


class ReceiptSerializer(ModelSerializer):

    class Meta:
        model = Receipt
        fields = '__all__'


class OrderSerializer(ModelSerializer):

    ticket = TicketSerializer(many=False, read_only=True)
    customer = CustomerSerializer(many=False, read_only=True)
    receipts = ReceiptSerializer(many=True, read_only=True, source='receipt_set')

    class Meta:
        model = Order
        fields = ['id', 'customer', 'ticket', 'date', 'count', 'cost', 'state', 'receipts']


class ReserveTicketSerializer(ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['count']
