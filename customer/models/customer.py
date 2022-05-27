import datetime

from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Customer(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='customer'
    )
    first_name = models.CharField(
        max_length=220,
    )
    last_name = models.CharField(
        max_length=220,
    )
    email = models.EmailField(
        unique=True,
        null=True,
        blank=True,
    )
    national_code = models.CharField(
        max_length=12
    )
    birth_date = models.DateTimeField(
        default=datetime.datetime.now
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
