from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from ticket.models import Ticket, Order
from ticket.serializers import TicketSerializer, OrderSerializer
from ticket.filters import TicketFilter


class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    http_method_names = ['get']
    filterset_class = TicketFilter


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    http_method_names = ['get']

    def get_queryset(self):
        return self.queryset.filter(customer__user=self.request.user)
