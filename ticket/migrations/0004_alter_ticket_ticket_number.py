# Generated by Django 4.0.4 on 2022-05-22 03:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0003_alter_company_phone_alter_ticket_ticket_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ticket_number',
            field=models.UUIDField(default=uuid.UUID('3a624516-4df5-4fed-8547-ac4300eed185'), editable=False),
        ),
    ]