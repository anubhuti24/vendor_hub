from django.urls import path
from vendor.views import (
    VendorCreateList, VendorFetchUpdateDelete
)

urlpatterns = [
    path("vendors/", VendorCreateList.as_view(), name="create_po"),
    path("vendors/<str:vendor_code>/", VendorFetchUpdateDelete.as_view(), name="po_detail"),
]
