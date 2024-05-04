from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from purchase_order.models import PurchaseOrderModel
from purchase_order.serializers import PurchaseOrderSerializer


class PurchaseOrderCreateList(APIView):
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
                    "message": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def post(self, request):
        try:
            serializer = PurchaseOrderSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"status": "True", "message": "Purchase Order created successfully!"},
                    status=status.HTTP_201_CREATED,
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": "False", "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PurchaseOrderFetchUpdateDelete(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, po_id):
        try:
            purchase_order = PurchaseOrderModel.objects.get(pk=po_id)
            serializer = PurchaseOrderSerializer(purchase_order)
            return Response(
                {"status": "True", "purchase order": serializer.data},
                status=status.HTTP_200_OK,
            )

        except ObjectDoesNotExist:
            return Response(
                {"status": "False", "message": "Object does not exists."},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            return Response({"status": "False", "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, po_id):
        try:
            purchase_order = PurchaseOrderModel.objects.filter(po_number=po_id).first()
            print("Purchase order", purchase_order)
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
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except ObjectDoesNotExist:
            return Response(
                {"status": "False", "message": "Object does not exist."},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            return Response({"status": "False", "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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
        except Exception as e:
            return Response({"status": "False", "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
