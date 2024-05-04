from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils import timezone

from purchase_order.models import PurchaseOrderModel


@receiver(post_save, sender=PurchaseOrderModel)
def update_performance_metrics(sender, instance, created, **kwargs):
    if not created:
        # Update performance metrics when PurchaseOrder is updated
        if instance.status == PurchaseOrderModel.COMPLETED:
            print("Here")
            update_on_time_delivery_rate(instance)
            update_quality_rating_avg(instance)
        # Calculated upon any change in PO status
        update_fulfillment_rate(instance)


@receiver(pre_save, sender=PurchaseOrderModel)
def update_acknowledgment_date(sender, instance, **kwargs):
    if instance.pk is None:
        # Set acknowledgment_date for new PurchaseOrder
        instance.acknowledgment_date = timezone.now()
    else:
        # Update average_response_time when PurchaseOrder is updated
        if instance.acknowledgment_date is None:
            instance.acknowledgment_date = timezone.now()
            update_average_response_time(instance)


def update_on_time_delivery_rate(instance):
    vendor = instance.vendor
    completed_orders = PurchaseOrderModel.objects.filter(vendor=vendor, status=PurchaseOrderModel.COMPLETED)
    on_time_orders = completed_orders.filter(delivery_date__gte=instance.delivery_date)
    on_time_delivery_rate = (on_time_orders.count() / completed_orders.count()) * 100 if completed_orders.count() > 0 else 0
    vendor.on_time_delivery_rate = on_time_delivery_rate
    vendor.save()


def update_quality_rating_avg(instance):
    vendor = instance.vendor
    completed_orders = PurchaseOrderModel.objects.filter(vendor=vendor, status=PurchaseOrderModel.COMPLETED)
    total_quality_rating = sum(order.quality_rating for order in completed_orders)
    quality_rating_avg = total_quality_rating / completed_orders.count() if completed_orders.count() > 0 else 0
    vendor.quality_rating_avg = quality_rating_avg
    vendor.save()


def update_average_response_time(instance):
    vendor = instance.vendor
    completed_orders = PurchaseOrderModel.objects.filter(vendor=vendor, status=PurchaseOrderModel.COMPLETED)
    total_response_time = sum((order.acknowledgment_date - order.issue_date).total_seconds() for order in completed_orders)
    average_response_time = total_response_time / completed_orders.count() if completed_orders.count() > 0 else 0
    vendor.average_response_time = average_response_time
    vendor.save()


def update_fulfillment_rate(instance):
    vendor = instance.vendor
    all_orders = PurchaseOrderModel.objects.filter(vendor=vendor)
    completed_orders = all_orders.filter(status=PurchaseOrderModel.COMPLETED)
    fulfilled_orders = completed_orders.filter(quality_rating__gt=0)
    fulfillment_rate = (fulfilled_orders.count() / all_orders.count()) * 100 if all_orders.count() > 0 else 0
    vendor.fulfillment_rate = fulfillment_rate
    vendor.save()
