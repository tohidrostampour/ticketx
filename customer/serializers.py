from rest_framework.serializers import ModelSerializer

from customer.models import Customer


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        read_only_fields = ('email', 'user', 'is_registered')
