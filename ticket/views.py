from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from ticket.models import Ticket, Order
from ticket.permissions import IsOrderOwner
from ticket.serializers import TicketSerializer, OrderSerializer


class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    http_method_names = ['get']


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    http_method_names = ['get']
    # permission_classes = [IsOrderOwner]

    def get_queryset(self):
        return self.queryset.filter(customer__user=self.request.user)
