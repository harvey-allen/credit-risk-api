from django.urls import path, include
from rest_framework.routers import DefaultRouter
from calculate.api.viewsets import CreditParametersViewSet

router = DefaultRouter()
router.register(r'credit-parameters', CreditParametersViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
