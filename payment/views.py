from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from payment.models import Wallet
from payment.serializers import WalletSerializer


class WalletRetrieveApiView(RetrieveAPIView):
    serializer_class = WalletSerializer
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, *args, **kwargs):
        wallet = Wallet.objects.get(user=request.user)
        serializer = self.serializer_class(wallet)

        return Response(serializer.data)


class WalletUpdateApiView(UpdateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    permission_classes = (IsAuthenticated,)
