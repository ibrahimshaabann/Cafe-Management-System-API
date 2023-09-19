from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuApiView, TableApiView, CategoryApiView, OrderApiView, OrderItemApiView, last_active_orders

router = DefaultRouter()
router.register(r'menu', MenuApiView)
router.register(r'table', TableApiView)
router.register(r'category', CategoryApiView)
router.register(r'order', OrderApiView)
router.register(r'orderitem', OrderItemApiView)
router.register(r'active_orders', last_active_orders, basename='last-active-orders')


urlpatterns = [
    path('', include(router.urls)),
]
