from django.core.exceptions import ValidationError


def product_quantity_validator(value):

    if value < 0:
        raise ValidationError('Quantity must be positive integer!')