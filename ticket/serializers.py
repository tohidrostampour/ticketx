from rest_framework.serializers import ModelSerializer

from ticket.models import Ticket, Order


class TicketSerializer(ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'
        read_only_fields = ('user',)


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
