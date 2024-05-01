from django.urls import path
from .views import (
    VendorCreateAPIView,
    VendorListAPIView,
    VendorDetailAPIView,
    VendorUpdateAPIView,
    VendorDeleteAPIView,
)


urlpatterns = [
    path('vendors/', VendorCreateAPIView.as_view(), name='create_vendor'),
    path('vendors/', VendorListAPIView.as_view(), name='list_vendors'),
    path('vendors/<str:vendor_code>/', VendorDetailAPIView.as_view(), name='vendor_detail'),
    path('vendors/<str:vendor_code>/', VendorUpdateAPIView.as_view(), name='update_vendor'),
    path('vendors/<str:vendor_code>/', VendorDeleteAPIView.as_view(), name='delete_vendor'),
]
