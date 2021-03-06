from django.core.exceptions import ValidationError
from django.db import models

from utils.base_model import BaseModel
from ticket.validators import validate_count, validate_price


class Ticket(BaseModel):
    class Type(models.IntegerChoices):
        BUS = 0, 'Bus'
        TRAIN = 1, 'Train'
        Airplane = 2, 'Airplane'

    title = models.CharField(
        max_length=220,
    )
    company = models.CharField(
        max_length=220
    )
    departure = models.CharField(
        max_length=220,
    )
    destination = models.CharField(
        max_length=220,
    )
    start_time = models.DateField()
    end_time = models.DateField()
    count = models.IntegerField(validators=[validate_count])
    type = models.IntegerField(
        choices=Type.choices,
        default=Type.BUS,
    )
    price = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        validators=[validate_price],
        null=True
    )

    code = models.CharField(
        max_length=20,
    )

    def _validate_start_end_dates(self):
        if self.end_time < self.start_time:
            raise ValidationError("End date cannot be before start date.")

    def save(self, *args, **kwargs):
        self._validate_start_end_dates()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}: {self.departure} - {self.destination}"
