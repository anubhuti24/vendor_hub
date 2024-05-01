from django.urls import path
from .views import (
    VendorCreateAPIView,
    VendorListAPIView,
    VendorDetailAPIView,
    VendorUpdateAPIView,
    VendorDeleteAPIView,
)


urlpatterns = [
    path('vendors/create/', VendorCreateAPIView.as_view(), name='create_vendor'),
    path('vendors/list/', VendorListAPIView.as_view(), name='list_vendors'),
    path('vendors/<str:vendor_code>/', VendorDetailAPIView.as_view(), name='vendor_detail'),
    path('vendors/<str:vendor_code>/update/', VendorUpdateAPIView.as_view(), name='update_vendor'),
    path('vendors/<str:vendor_code>/delete/', VendorDeleteAPIView.as_view(), name='delete_vendor'),
]