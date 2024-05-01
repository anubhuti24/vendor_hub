from django.urls import path

from purchase_order.views import (
    PurchaseOrderCreateAPIView,
    PurchaseOrderListAPIView,
    PurchaseOrderDetailAPIView,
    PurchaseOrderUpdateAPIView,
    PurchaseOrderDeleteAPIView,
)

urlpatterns = [
    path("create/", PurchaseOrderCreateAPIView.as_view(), name="create_po"),
    path("list/", PurchaseOrderListAPIView.as_view(), name="po_list"),
    path("get/<str:po_id>/", PurchaseOrderDetailAPIView.as_view(), name="po_detail"),
    path("update/<str:po_id>/", PurchaseOrderUpdateAPIView.as_view(), name="update_po"),
    path("remove/<str:po_id>/", PurchaseOrderDeleteAPIView.as_view(), name="delete_po"),
]
