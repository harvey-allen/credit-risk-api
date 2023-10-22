import pickle
import logging

from django.db import transaction
from rest_framework import viewsets

from calculate.api.serializers import CreditParametersSerializer
from calculate.models import CreditParameters


class CreditParametersViewSet(viewsets.ModelViewSet):

    log = logging.getLogger('credit_parameters')

    queryset = CreditParameters.objects.all()
    serializer_class = CreditParametersSerializer

    def perform_create(self, serializer):
        filename = "credit_model.sav"
        model = pickle.load(open(filename, "rb"))
        data = serializer.validated_data
        credit_prediction = model.predict(data)
        with transaction.atomic():
            self.log.info(f"{data[id]} has a predicted credit score of {credit_prediction}.")
            data["credit_score"] = credit_prediction
            serializer.save()
