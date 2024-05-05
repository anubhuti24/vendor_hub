from django.utils import timezone


def validate_delivery_date(value):
    if value < timezone.now():
        raise ValueError("Delivery date cannot be in the past.")


def validate_items(value):
    if not value:
        raise ValueError("Items cannot be empty.")


def validate_acknowledgment_date(value):
    if value < timezone.now():
        raise ValueError("Acknowledgment date cannot be in the past.")
