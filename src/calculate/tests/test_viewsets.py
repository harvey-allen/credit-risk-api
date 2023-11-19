import json
from unittest.mock import patch

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from calculate.models import CreditParameters


class CreditParametersViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = "/calculate/"

    @patch("your_app.views.open")
    def test_create_credit_parameters(self, mock_open):
        mock_model = patch("your_app.views.pickle.load").start()
        mock_model.return_value.predict.return_value = 750
        mock_open.return_value = open("model.sav", "rb")
        data = {}
        response = self.client.post(self.url, json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        credit_parameters = CreditParameters.objects.get(id=response.data["id"])
        self.assertEqual(credit_parameters.credit_score, 750)

    def test_retrieve_credit_parameters(self):
        credit_parameters = CreditParameters.objects.create(your_data_field="value")
        response = self.client.get(f"{self.url}{credit_parameters.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["your_data_field"], "value")

    def test_update_credit_parameters(self):
        credit_parameters = CreditParameters.objects.create(your_data_field="value")
        updated_data = {}
        response = self.client.put(f"{self.url}{credit_parameters.id}/", json.dumps(updated_data),
                                   content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        credit_parameters.refresh_from_db()
        self.assertEqual(credit_parameters.your_data_field, "new_value")

    def test_delete_credit_parameters(self):
        credit_parameters = CreditParameters.objects.create(your_data_field="value")
        response = self.client.delete(f"{self.url}{credit_parameters.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(CreditParameters.DoesNotExist):
            CreditParameters.objects.get(id=credit_parameters.id)
