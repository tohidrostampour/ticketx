from rest_framework.viewsets import ModelViewSet

from ticket.models import Ticket
from ticket.serializers import TicketSerializer


class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    