from django.contrib import admin

from ticket.models import Ticket, Order

admin.site.register(Ticket)
admin.site.register(Order)


