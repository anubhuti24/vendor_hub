from django.contrib import admin
from vendor.models import VendorProfile, HistoricalModel


@admin.register(VendorProfile)
class VendorAdmin(admin.ModelAdmin):
    list_display = ["vendor_code", "name", "contact_details", "address",
                    "on_time_delivery_rate", "quality_rating_avg", "average_response_time", "fulfillment_rate"]


@admin.register(HistoricalModel)
class HistoricDataAdmin(admin.ModelAdmin):
    list_display = ["vendor", "date", "on_time_delivery_rate", "quality_rating_avg",
                    "average_response_time", "fulfillment_rate"]
