from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuApiView,TableApiView,CategoryApiView

router = DefaultRouter()
router.register(r'menu', MenuApiView)
router.register(r'table',TableApiView)
router.register(r'category',CategoryApiView)

urlpatterns = [
    path('', include(router.urls)),
]

