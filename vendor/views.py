from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from vendor.models import VendorProfile
from vendor.serializers import VendorProfileSerializer


class VendorCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = VendorProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "True", "message": "Vendor created successfully!"},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VendorListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        vendors = VendorProfile.objects.all()
        serializer = VendorProfileSerializer(vendors, many=True)
        return Response(serializer.data)


class VendorDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, vendor_code):
        vendor = get_object_or_404(VendorProfile, vendor_code=vendor_code)
        serializer = VendorProfileSerializer(vendor)
        return Response({"status": "True", "vendor": serializer.data},
                        status=status.HTTP_201_CREATED)


class VendorUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, vendor_code):
        vendor = get_object_or_404(VendorProfile, vendor_code=vendor_code)
        serializer = VendorProfileSerializer(vendor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "True", "updated_vendor": serializer.data},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VendorDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, vendor_code):
        vendor = get_object_or_404(VendorProfile, vendor_code=vendor_code)
        vendor.delete()
        return Response({"status": "True", "message": "Vendor deleted successfully"},
                        status=status.HTTP_201_CREATED)
