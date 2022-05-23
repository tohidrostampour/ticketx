from django.urls import path, include
from rest_framework import routers

from ticket.views import TicketViewSet

router = routers.DefaultRouter()
router.register(r'ticket', TicketViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
