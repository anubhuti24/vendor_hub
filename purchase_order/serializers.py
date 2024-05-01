from rest_framework import serializers

from purchase_order.models import PurchaseOrderModel


class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrderModel
        fields = "__all__"
