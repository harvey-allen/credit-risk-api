from rest_framework import serializers

from calculate.models import CreditParameters


class CreditParametersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditParameters
        fields = "__all__"

    def validate(self, attrs):
        pass
