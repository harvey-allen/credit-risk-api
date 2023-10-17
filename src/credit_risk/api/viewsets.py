import pickle

from rest_framework import viewsets

from src.credit_risk.api.serializers import CreditParametersSerializer
from src.credit_risk.models import CreditParameters


class CreditParametersViewSet(viewsets.ModelViewSet):

    queryset = CreditParameters.objects.all()
    serializer_class = CreditParametersSerializer

    def perform_create(self, serializer):
        filename = "credit_model.sav"
        model = pickle.load(open(filename, "rb"))
        data = serializer.validated_data
        data["credit_score"] = model.predict(data)
        serializer.save()
