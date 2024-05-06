import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class PurchaseOrderAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='aaa', password='11')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')

    def test_purchase_order_endpoints(self):
        """
        Test Cases for create, get, update, delete a purchase order and acknowledge a purchase order
        """

        # Create a vendor
        vendor_response = self.client.post('/api/vendors/', {
            "name": "James Willie",
            "contact_details": "9899888898",
            "address": "6/12 Robert House",
            "vendor_code": "VENDOR001"
        })
        self.assertEqual(vendor_response.status_code, status.HTTP_201_CREATED)

        # Test POST request to create a new purchase order
        response = self.client.post('/api/purchase_orders/', {
          "po_number": "PO99",
          "vendor": "VENDOR001",
          "order_date": "2024-05-01T12:00:00Z",
          "delivery_date": "2024-05-10T12:00:00Z",
          "items": json.dumps([
            {
              "name": "Item 1",
              "quantity": 10,
              "unit_price": 20
            },
            {
              "name": "Item 2",
              "quantity": 5,
              "unit_price": 30
            }
          ]),
          "quantity": 10,
          "status": "PENDING",
          "quality_rating": 3.5,
          "issue_date": "2024-05-10T12:00:00Z",
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Test GET request to retrieve all purchase orders
        response = self.client.get('/api/purchase_orders/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test PUT request to update a purchase order
        response = self.client.put(f'/api/purchase_orders/PO99/', {
          "po_number": "PO99",
          "vendor": "VENDOR001",
          "order_date": "2024-05-01T12:00:00Z",
          "delivery_date": "2024-05-10T12:00:00Z",
          "items": json.dumps([
            {
              "name": "Item 10",
              "quantity": 10,
              "unit_price": 20
            }
          ]),
          "quantity": 10,
          "status": "COMPLETED",
          "quality_rating": 3.5,
          "issue_date": "2024-05-10T12:00:00Z",
          "acknowledgment_date": "2024-05-15T12:00:00Z"
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test POST request to acknowledge a purchase order
        response = self.client.post(f'/api/purchase_orders/PO99/acknowledge/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test DELETE request to delete a purchase order
        response = self.client.delete(f'/api/purchase_orders/PO99/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
