from rest_framework import serializers

from src.credit_risk.models import CreditParameters


class CreditParametersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditParameters
        fields = "__all__"
