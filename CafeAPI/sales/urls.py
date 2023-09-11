from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuApiView

router = DefaultRouter()
router.register(r'menu', MenuApiView)

urlpatterns = [
    path('', include(router.urls)),
]

