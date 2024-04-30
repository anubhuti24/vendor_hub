from django.db import models


class VendorProfile(models.Model):
    name = models.CharField(max_length=20)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True, primary_key=True)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return f"{self.name} {self.vendor_code}"


class PurchaseOrderModel(models.Model):
    PENDING = "PEN"
    COMPLETED = "COM"
    CANCELLED = "CAN"
    OrderStatus = {
        PENDING: "PENDING",
        COMPLETED: "COMPLETED",
        CANCELLED: "CANCELLED"
    }

    po_number = models.CharField(max_length=50, unique=True, primary_key=True)
    vendor = models.ForeignKey(VendorProfile, on_delete=models.CASCADE, related_name="purchase_order")
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=10, choices=OrderStatus, default=PENDING)
    quality_rating = models.FloatField()
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField()

    def __str__(self):
        return f"{self.po_number}"


class HistoricalModel(models.Model):
    vendor = models.ForeignKey(VendorProfile, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()
