from django.core.exceptions import ValidationError


def validate_count(value):
    if value < 0:
        raise ValidationError(
            "Count cannot be negative or 0."
        )


def validate_price(value):
    if value < 0:
        raise ValidationError(
            "Price cannot be negative."
        )
