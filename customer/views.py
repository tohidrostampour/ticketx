from rest_framework.viewsets import ModelViewSet

from customer.models import Customer
from customer.serializers import CustomerSerializer
from customer.permissions import IsCustomerOrAdmin


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    http_method_names = ['get', 'put']
    permission_classes = [IsCustomerOrAdmin]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.queryset.filter(user=self.request.user)

