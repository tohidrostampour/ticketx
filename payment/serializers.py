from rest_framework.serializers import ModelSerializer
from payment.models import Wallet


class WalletSerializer(ModelSerializer):
    class Meta:
        model = Wallet
        fields = '__all__'
        read_only_fields = ('id', 'user')

    def update(self, instance, validated_data):
        instance.amount += validated_data.get('amount')
        instance.save()

        return instance
