from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from vendor.models import VendorProfile
from vendor.serializers import VendorProfileSerializer


class VendorCreateList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            vendors = VendorProfile.objects.all()
            serializer = VendorProfileSerializer(vendors, many=True)
            return Response(
                {"status": "True", "vendors": serializer.data}, status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response({"status": "False", "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = VendorProfileSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "True", "message": "Vendor created successfully!"},
                                status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": "False", "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class VendorFetchUpdateDelete(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, vendor_code):
        try:
            vendor = VendorProfile.objects.get(pk=vendor_code)
            serializer = VendorProfileSerializer(vendor)
            return Response(
                {"status": "True", "vendor": serializer.data},
                status=status.HTTP_200_OK,
            )

        except ObjectDoesNotExist:
            return Response(
                {"status": "False", "message": "Vendor does not exists."},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            return Response({"status": "False", "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, vendor_code):
        try:
            vendor = VendorProfile.objects.get(pk=vendor_code)
            serializer = VendorProfileSerializer(vendor, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "True", "updated_vendor": serializer.data}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except ObjectDoesNotExist:
            return Response(
                {"status": "False", "message": "Vendor does not exist."},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            return Response({"status": "False", "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, vendor_code):
        try:
            vendor = VendorProfile.objects.get(pk=vendor_code)
            vendor.delete()
            return Response({"status": "True", "message": "Vendor deleted successfully"}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response(
                {"status": "False", "message": "Object does not exist."},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            return Response({"status": "False", "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class VendorPerformanceMetrics(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, vendor_id):
        try:
            vendor = VendorProfile.objects.get(vendor_code=vendor_id)
            serializer = VendorProfileSerializer(vendor)
            performance_data = {
                'on_time_delivery_rate': vendor.on_time_delivery_rate,
                'quality_rating_avg': vendor.quality_rating_avg,
                'average_response_time': vendor.average_response_time,
                'fulfillment_rate': vendor.fulfillment_rate,
            }
            return Response({'status': 'True', 'performance': performance_data}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'status': 'False', 'message': 'Vendor not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'status': 'False', 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
