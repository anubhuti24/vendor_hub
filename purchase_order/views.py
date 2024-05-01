from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from purchase_order.models import PurchaseOrderModel
from purchase_order.serializers import PurchaseOrderSerializer


class PurchaseOrderCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PurchaseOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": "True", "message": "Purchase Order created successfully!"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PurchaseOrderListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            vendor = request.query_params.get("vendor", None)
            if vendor:
                purchase_orders = PurchaseOrderModel.objects.filter(vendor=vendor)
            else:
                purchase_orders = PurchaseOrderModel.objects.all()

            serializer = PurchaseOrderSerializer(purchase_orders, many=True)
            return Response(
                {"status": "True", "order": serializer.data}, status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {
                    "status": "False",
                    "message": "An error occurred while processing your request.",
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class PurchaseOrderDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, po_id):
        try:
            purchase_order = PurchaseOrderModel.objects.get(pk=po_id)
            serializer = PurchaseOrderSerializer(purchase_order)
        except ObjectDoesNotExist:
            return Response(
                {"status": "False", "message": "Object does not exists."},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(
            {"status": "True", "purchase order": serializer.data},
            status=status.HTTP_200_OK,
        )


class PurchaseOrderUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, po_id):
        try:
            purchase_order = PurchaseOrderModel.objects.get(pk=po_id)
            serializer = PurchaseOrderSerializer(purchase_order, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "status": "True",
                        "message": "Purchase order updated successfully.",
                    },
                    status=status.HTTP_200_OK,
                )
        except ObjectDoesNotExist:
            return Response(
                {"status": "False", "message": "Object does not exist."},
                status=status.HTTP_404_NOT_FOUND,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PurchaseOrderDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, po_id):
        try:
            purchase_order = PurchaseOrderModel.objects.get(pk=po_id)
            purchase_order.delete()
            return Response(
                {"status": "True", "message": "Purchase order deleted successfully."},
                status=status.HTTP_200_OK,
            )
        except ObjectDoesNotExist:
            return Response(
                {"status": "False", "message": "Object does not exist."},
                status=status.HTTP_404_NOT_FOUND,
            )