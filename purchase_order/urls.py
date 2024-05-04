from django.urls import path
from purchase_order.views import (
    PurchaseOrderCreateList, PurchaseOrderFetchUpdateDelete, PurchaseOrderAcknowledge
)

urlpatterns = [
    path("purchase_orders/", PurchaseOrderCreateList.as_view(), name="create_po"),
    path("purchase_orders/<str:po_id>/", PurchaseOrderFetchUpdateDelete.as_view(), name="po_detail"),
    path("purchase_orders/<str:po_id>/acknowledge/", PurchaseOrderAcknowledge.as_view(),
         name='purchase-order-acknowledge'),
]
