from django_filters import rest_framework as filters

from ticket.models import Ticket


class TicketFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Ticket
        fields = ('departure', 'destination', 'start_time', 'end_time', 'type', 'min_price', 'max_price')