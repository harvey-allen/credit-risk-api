import factory

from calculate.models import CreditParameters


class CreditParametersFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CreditParameters

    id = factory.Faker("uuid4")
    name = factory.Faker("name")
    month = factory.Faker("date_this_month")
    occupation = factory.Faker("job")
