import logging

from rest_framework import serializers

from calculate.models import CreditParameters


class CreditParametersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditParameters
        fields = "__all__"

    log = logging.getLogger("credit_parameters")

    categorical_fields = [
        "name",
        "month",
        "occupation",
        "type_of_loans",
        "delay_from_due_date",
        "credit_mix",
        "payment_of_minimum_amount",
        "payment_behaviour",
        "changed_credit_limit",
        "credit_history_age",
    ]
    numerical_fields = [
        "age",
        "annual_income",
        "monthly_in_hand_salary",
        "number_of_bank_accounts",
        "number_of_credit_cards",
        "interest_rate",
        "number_of_loans",
        "number_of_delayed_payments",
        "number_of_credit_inquiries",
        "outstanding_debt",
        "credit_utilization_ratio",
        "total_emi_per_month",
        "amount_invested_monthly",
        "monthly_balance",
    ]

    def validate(self, data):
        for field in self.categorical_fields:
            if field not in data:
                self.log.error(f"categorical {field} is missing.")
                raise serializers.ValidationError(f"categorical {field} is required.")
        for field in self.numerical_fields:
            if field not in data:
                self.log.error(f"numerical {field} is missing.")
                raise serializers.ValidationError(f"numerical {field} is required.")
        return data

    def clean(self):
        cleaned_data = super().clean()

        for field in self.numerical_fields:
            if field in cleaned_data:
                cleaned_data[field] = round(cleaned_data[field], 2)
                self.log.info(
                    f"numerical {field} has been rounded to 2 decimal places."
                )

        return cleaned_data
