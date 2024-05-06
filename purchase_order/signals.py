from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils import timezone

from purchase_order.models import PurchaseOrderModel
from vendor.models import HistoricalModel

historical_data_saved = False


@receiver(post_save, sender=PurchaseOrderModel)
def update_performance_metrics(sender, instance, created, **kwargs):
    global historical_data_saved

    if not created:
        # Update performance metrics when PurchaseOrder is updated
        if instance.status == PurchaseOrderModel.COMPLETED:
            update_on_time_delivery_rate(instance)
            update_quality_rating_avg(instance)

        # Calculated upon any change in PO status
        update_fulfillment_rate(instance)

        if not created:
            if instance.acknowledgment_date is not None:
                update_average_response_time(instance.vendor)

        if not historical_data_saved:
            save_historical_data(instance.vendor)
            historical_data_saved = True


@receiver(pre_save, sender=PurchaseOrderModel)
def update_acknowledgment_date(sender, instance, **kwargs):
    global historical_data_saved

    # Set acknowledgment_date for new PurchaseOrder
    if instance.acknowledgment_date is None:
        instance.acknowledgment_date = timezone.now()
        update_average_response_time(instance)
    update_fulfillment_rate(instance)

    if not historical_data_saved:
        save_historical_data(instance.vendor)
        historical_data_saved = True


def update_on_time_delivery_rate(instance):
    """
    Calculate on-time delivery date
    """
    vendor = instance.vendor
    completed_orders = PurchaseOrderModel.objects.filter(vendor=vendor, status=PurchaseOrderModel.COMPLETED)
    on_time_orders = completed_orders.filter(delivery_date__lte=instance.delivery_date)
    on_time_delivery_rate = (on_time_orders.count() / completed_orders.count()) * 100 if completed_orders.count() > 0 else 0
    vendor.on_time_delivery_rate = on_time_delivery_rate
    vendor.save()


def update_quality_rating_avg(instance):
    """
    Calculate average quality rating
    """
    vendor = instance.vendor

    if instance.quality_rating:
        completed_orders = PurchaseOrderModel.objects.filter(vendor=vendor, status=PurchaseOrderModel.COMPLETED)
        total_quality_rating = sum(order.quality_rating for order in completed_orders)
        quality_rating_avg = total_quality_rating / completed_orders.count() if completed_orders.count() > 0 else 0
        vendor.quality_rating_avg = quality_rating_avg
        vendor.save()


def update_average_response_time(instance):
    """
    Calculate average response time
    """
    vendor = instance.vendor
    all_orders = PurchaseOrderModel.objects.filter(vendor=vendor)
    total_response_time = 0
    acknowledged_count = 0

    for order in all_orders:
        if order.acknowledgment_date is not None:
            response_time = (order.issue_date - order.acknowledgment_date).total_seconds() / 3600
            total_response_time += response_time
            acknowledged_count += 1

    average_response_time = total_response_time / acknowledged_count if acknowledged_count > 0 else 0
    vendor.average_response_time = average_response_time
    vendor.save()


def update_fulfillment_rate(instance):
    """
    Calculate the fulfillment rate
    """
    vendor = instance.vendor
    all_orders = PurchaseOrderModel.objects.filter(vendor=vendor)
    completed_orders = all_orders.filter(status=PurchaseOrderModel.COMPLETED)
    fulfilled_orders = completed_orders.filter(quality_rating__gt=0)
    fulfillment_rate = (fulfilled_orders.count() / all_orders.count()) * 100 if all_orders.count() > 0 else 0
    vendor.fulfillment_rate = fulfillment_rate
    vendor.save()


def save_historical_data(vendor):
    """
    Saves Historical data of the vendor
    """
    HistoricalModel.objects.create(
        vendor=vendor,
        date=timezone.now(),
        on_time_delivery_rate=vendor.on_time_delivery_rate,
        quality_rating_avg=vendor.quality_rating_avg,
        average_response_time=vendor.average_response_time,
        fulfillment_rate=vendor.fulfillment_rate
    )
