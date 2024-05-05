from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from purchase_order.helper import validate_delivery_date, validate_items, validate_acknowledgment_date
from vendor.models import VendorProfile


class PurchaseOrderModel(models.Model):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"
    OrderStatus = {PENDING: "PENDING", COMPLETED: "COMPLETED", CANCELLED: "CANCELLED"}

    po_number = models.CharField(max_length=50, unique=True, primary_key=True)
    vendor = models.ForeignKey(
        VendorProfile, on_delete=models.CASCADE, related_name="purchase_order"
    )
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField(validators=[validate_delivery_date])
    items = models.JSONField(validators=[validate_items])
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    status = models.CharField(max_length=10, choices=OrderStatus, default=PENDING)
    quality_rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True, validators=[validate_acknowledgment_date])

    def __str__(self):
        return f"{self.po_number}"
