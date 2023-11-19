import logging

from django.contrib import admin

from calculate.models import CreditParameters


@admin.register(CreditParameters)
class CreditParametersAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "age",
        "occupation",
        "payment_behaviour",
        "number_of_loans",
        "annual_income",
        "credit_score",
    )
    search_fields = ("name", "occupation")
    ordering = ("-credit_score",)

    log = logging.getLogger("credit_parameters")

    def save_model(self, request, obj, form, change):
        if change:
            original_obj = CreditParameters.objects.get(pk=obj.pk)
            self.log.info(
                f"{obj.id} has had a credit score update from {original_obj.credit_score} to {obj.credit_score}"
            )
        super().save_model(request, obj, form, change)
