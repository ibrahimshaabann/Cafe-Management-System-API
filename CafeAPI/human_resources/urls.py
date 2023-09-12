from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, AttendenceViewSet, CustomerViewSet, ShiftViewSet, SalaryDeduction
from django.urls import include, path

customers_router = DefaultRouter()
customers_router.register(r'customers', CustomerViewSet,  basename='customers')
attendence_router = DefaultRouter()
attendence_router.register(r'attendence', AttendenceViewSet,  basename='attendence')


# router.register(r'attendence', AttendenceViewSet,  basename='attendence')
# router.register(r'shifts', ShiftViewSet,  basename='shifts')
# router.register(r'employees', EmployeeViewSet,  basename='employees')
# router.register(r'deductions', SalaryDeduction, basename='deductions')

urlpatterns = [
    path('',include(customers_router.urls)),
    path('',include(attendence_router.urls))
]