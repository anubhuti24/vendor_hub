from rest_framework import serializers

from purchase_order.models import PurchaseOrderModel


class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrderModel
        fields = [
            'po_number',
            'vendor',
            'order_date',
            'delivery_date',
            'items',
            'quantity',
            'status',
            'quality_rating',
            'issue_date',
            'acknowledgment_date',
        ]

    def update(self, instance, validated_data):
        instance.vendor = validated_data.get('vendor', instance.vendor)
        instance.order_date = validated_data.get('order_date', instance.order_date)
        instance.delivery_date = validated_data.get('delivery_date', instance.delivery_date)
        instance.items = validated_data.get('items', instance.items)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.status = validated_data.get('status', instance.status)
        instance.quality_rating = validated_data.get('quality_rating', instance.quality_rating)
        instance.issue_date = validated_data.get('issue_date', instance.issue_date)
        instance.acknowledgment_date = validated_data.get('acknowledgment_date', instance.acknowledgment_date)
        instance.save()
        return instance
