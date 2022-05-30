import random
from django.core.management.base import BaseCommand
from faker import Faker
from faker.providers.address.fa_IR import Provider as AddressProvider
from faker.providers.company.fa_IR import Provider as CompanyProvider
from ticket.models import Ticket
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = "adds 50 random generated tickets"

    def handle(self, *args, **kwargs):
        fake = Faker()
        fake.add_provider(AddressProvider)
        fake.add_provider(CompanyProvider)

        types = {
            0: "اتوبوس",
            1: "قطار",
            2: "هواپیما",
        }
        tickets = []

        for i in range(50):
            dep_city = fake.state()
            dest_city = fake.state()
            company = fake.company()
            type = random.randint(0, 2)
            start_time = datetime.today() + timedelta(days=random.randint(1, 10))
            end_time = start_time + timedelta(days=random.randint(0, 3))

            ticket = Ticket(
                title=f"بلیت {types[type] } از {dep_city} به {dest_city}",
                company=company,
                departure=dep_city,
                destination=dest_city,
                start_time=start_time,
                end_time=end_time,
                type=type,
                price=random.randint(1, 5) * 10_000,
                code=fake.postcode(),
                count=random.randint(10, 30)
            )
            tickets.append(ticket)

        Ticket.objects.bulk_create(tickets)
