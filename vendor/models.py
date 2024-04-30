from django.db import models
from django.core.validators import RegexValidator


class VendorProfile(models.Model):
    name = models.CharField(max_length=20)
    phone_regex = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(unique=True, primary_key=True)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()
