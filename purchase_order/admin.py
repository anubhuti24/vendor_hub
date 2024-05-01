from django.contrib import admin

from purchase_order.models import PurchaseOrderModel


@admin.register(PurchaseOrderModel)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = [
        "po_number",
        "vendor",
        "order_date",
        "delivery_date",
        "items",
        "quantity",
        "status",
        "quality_rating",
        "issue_date",
        "acknowledgment_date",
    ]
