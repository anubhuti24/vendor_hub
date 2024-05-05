from django.db import models

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
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=10, choices=OrderStatus, default=PENDING)
    quality_rating = models.FloatField()
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.po_number}"
