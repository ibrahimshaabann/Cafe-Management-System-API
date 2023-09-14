from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CostsApiView,BenefitsApiView

router = DefaultRouter()
router.register(r'costs', CostsApiView)
router.register(r'benefits',BenefitsApiView)

urlpatterns = [
    path('', include(router.urls)),
]

