from django.urls import include, path
from rest_framework.routers import DefaultRouter

from calculate.api.viewsets import CreditParametersViewSet

router = DefaultRouter()
router.register(r"credit-parameters", CreditParametersViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
