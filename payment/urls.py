from django.urls import path
from payment.views import WalletRetrieveApiView, WalletUpdateApiView


urlpatterns = (
    path('user/wallet/', WalletRetrieveApiView.as_view()),
    path('wallet/<int:pk>', WalletUpdateApiView.as_view())
)
