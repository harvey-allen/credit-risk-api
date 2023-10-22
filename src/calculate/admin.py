from django.contrib import admin
from calculate.models import CreditParameters


class CreditParametersAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'occupation', 'payment_behaviour', 'number_of_loans', 'annual_income', 'credit_score')
    search_fields = ('name', 'occupation')
    ordering = ('-credit_score',)


admin.site.register(CreditParameters, CreditParametersAdmin)