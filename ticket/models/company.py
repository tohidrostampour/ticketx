from django.core.validators import RegexValidator
from django.db import models

from utils.base_model import BaseModel


class Company(BaseModel):
    class Meta:
        verbose_name_plural = 'Companies'

    name = models.CharField(
        max_length=220,
    )
    phone = models.CharField(
        max_length=220,
        validators=[
            RegexValidator(
                regex=r'^\+989\d{9}$|^09\d{9}$',
                message='phone number must be in iranian format',
                code='invalid_format'
            )]
    )

    def __str__(self):
        return f"{self.name}"
