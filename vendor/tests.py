from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class VendorAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='aaa', password='11')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')

    def test_vendors_endpoints(self):
        """
        Test Cases to create, get, update, delete a vendor and retrieve vendor's performance
        """

        # Test POST request to create a new vendor
        response = self.client.post('/api/vendors/', {
              "name": "James Willie",
              "contact_details": "7677778788",
              "address": "6/12 Robert House",
              "vendor_code": "VENDOR001"
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Test GET request to retrieve all vendors
        response = self.client.get('/api/vendors/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test PUT request to update a vendor
        response = self.client.put(f'/api/vendors/VENDOR001/', {
            "name": "XYZ",
            "contact_details": "9897806985",
            "address": "6/12 Robert House",
            "vendor_code": "VENDOR001"
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test GET request to retrieve performance metrics of a vendor
        response = self.client.get(f'/api/vendors/VENDOR001/performance/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test DELETE request to delete a vendor
        response = self.client.delete(f'/api/vendors/VENDOR001/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_nonexistent_vendor_fetch_update_delete(self):
        """
        Test Cases for 404 Not Found exception
        """

        # Test handling of nonexistent vendor
        response = self.client.get('/api/vendors/VENDOR092/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.put('/api/vendors/VENDOR092/', {
            "name": "Alice Walker",
            "contact_details": "9897806985",
            "address": "",
            "vendor_code": "VENDOR001"
        })
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.delete('/api/vendors/VENDOR092/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
