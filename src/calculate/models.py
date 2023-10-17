from django.db import models
from django.utils.translation import gettext_lazy as _


class CreditStatus(models.TextChoices):
    POOR = "poor", _("Poor Credit")
    STANDARD = "standard", _("Standard Credit")
    GOOD = "good", _("Good Credit")


class CreditParameters(models.Model):
    # Categorical Features
    name = models.CharField(max_length=100)
    month = models.CharField(max_length=10)
    occupation = models.CharField(max_length=100)
    type_of_loan = models.CharField(max_length=100)
    delay_from_due_date = models.CharField(max_length=10)
    credit_mix = models.CharField(max_length=100)
    payment_of_min_amount = models.CharField(max_length=10)
    payment_behaviour = models.CharField(max_length=100)
    changed_credit_limit = models.CharField(max_length=10)
    credit_history_age = models.CharField(max_length=100)
    # Numerical Features
    age = models.IntegerField()
    annual_income = models.DecimalField(max_digits=10, decimal_places=2)
    monthly_inhand_salary = models.DecimalField(max_digits=10, decimal_places=2)
    num_bank_accounts = models.IntegerField()
    num_credit_card = models.IntegerField()
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    num_of_loan = models.IntegerField()
    num_of_delayed_payment = models.IntegerField()
    num_credit_inquiries = models.IntegerField()
    outstanding_debt = models.DecimalField(max_digits=10, decimal_places=2)
    credit_utilization_ratio = models.DecimalField(max_digits=5, decimal_places=2)
    total_emi_per_month = models.DecimalField(max_digits=10, decimal_places=2)
    amount_invested_monthly = models.DecimalField(max_digits=10, decimal_places=2)
    monthly_balance = models.DecimalField(max_digits=10, decimal_places=2)
    # Result
    models.CharField(
        max_length=20,
        choices=CreditStatus.choices,
        verbose_name="qualification type",
        blank=True,
        null=True,
    )
