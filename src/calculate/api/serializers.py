from rest_framework import serializers

from calculate.models import CreditParameters


class CreditParametersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditParameters
        fields = "__all__"

    def validate(self, data):
        categorical_fields = [
            'name', 'month', 'occupation', 'type_of_loans', 'delay_from_due_date',
            'credit_mix', 'payment_of_minimum_amount', 'payment_behaviour',
            'changed_credit_limit', 'credit_history_age'
        ]
        numerical_fields = [
            'age', 'annual_income', 'monthly_in_hand_salary', 'number_of_bank_accounts',
            'number_of_credit_cards', 'interest_rate', 'number_of_loans', 'number_of_delayed_payments',
            'number_of_credit_inquiries', 'outstanding_debt', 'credit_utilization_ratio',
            'total_emi_per_month', 'amount_invested_monthly', 'monthly_balance'
        ]
        for field in categorical_fields:
            if field not in data:
                raise serializers.ValidationError(f"categorical {field} is required.")
        for field in numerical_fields:
            if field not in data:
                raise serializers.ValidationError(f"numerical {field} is required.")
        return data

    def clean(self):
        pass
