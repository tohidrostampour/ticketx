from django.urls import path, include
from rest_framework import routers

from ticket.views import TicketViewSet, OrderViewSet, ReserveTicketAPIView

router = routers.DefaultRouter()
router.register(r'ticket', TicketViewSet)
router.register(r'order', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('ticket/<int:pk>/reserve', ReserveTicketAPIView.as_view())

]
