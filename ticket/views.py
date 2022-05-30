from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import GenericAPIView

from ticket.models import Ticket, Order
from ticket.serializers import TicketSerializer, OrderSerializer, ReserveTicketSerializer
from ticket.filters import TicketFilter
from ticket.services import complete_order


class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    http_method_names = ['get']
    filterset_class = TicketFilter


class ReserveTicketAPIView(GenericAPIView):
    serializer_class = ReserveTicketSerializer

    def post(self, request, pk):
        serializer = self.serializer_class(data=request.data)
        ticket = get_object_or_404(Ticket, pk=pk)

        if serializer.is_valid():
            count = serializer.validated_data.get('count')
            order = Order.objects.create(customer=request.user.customer,
                                         ticket_id=pk,
                                         count=count,
                                         cost=ticket.price * count)
            complete_order(order, request.user.wallet.amount)

            return Response(OrderSerializer(order).data)


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    http_method_names = ['get']

    def get_queryset(self):
        return self.queryset.filter(customer__user=self.request.user)
