from django.core.validators import RegexValidator
from django.db import models


class VendorProfile(models.Model):
    name = models.CharField(max_length=20, validators=[RegexValidator(r'^[a-zA-Z\s]+$', 'Name should only contain letters and spaces.')])
    contact_details = models.TextField(validators=[RegexValidator(r'^[\d\+\-\(\)\s]+$', 'Contact details should only contain digits, spaces, and allowed characters (+, -, ())')])
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True, primary_key=True)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return f"{self.name} {self.vendor_code}"


class HistoricalModel(models.Model):
    vendor = models.ForeignKey(VendorProfile, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()
