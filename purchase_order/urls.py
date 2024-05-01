from django.urls import path

from purchase_order.views import (
    PurchaseOrderCreateAPIView,
    PurchaseOrderListAPIView,
    PurchaseOrderDetailAPIView,
    PurchaseOrderUpdateAPIView,
    PurchaseOrderDeleteAPIView,
)

urlpatterns = [
    path("purchase_orders/", PurchaseOrderCreateAPIView.as_view(), name="create_po"),
    path("purchase_orders/", PurchaseOrderListAPIView.as_view(), name="po_list"),
    path("purchase_orders/<str:po_id>/", PurchaseOrderDetailAPIView.as_view(), name="po_detail"),
    path("purchase_orders/<str:po_id>/", PurchaseOrderUpdateAPIView.as_view(), name="update_po"),
    path("purchase_orders/<str:po_id>/", PurchaseOrderDeleteAPIView.as_view(), name="delete_po"),
]
