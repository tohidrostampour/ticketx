from django.contrib import admin

from ticket.models import Ticket, Company

admin.site.register(Ticket)
admin.site.register(Company)
