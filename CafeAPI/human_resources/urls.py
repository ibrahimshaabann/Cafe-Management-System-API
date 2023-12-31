from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, AttendenceViewSet, CustomerViewSet, ShiftViewSet, SalaryDeductionViewSet
from django.urls import include, path, re_path
from rest_framework_swagger.views import get_swagger_view
    

router = DefaultRouter()
router.register(r'customers', CustomerViewSet,  basename='customers')
router.register(r'attendence', AttendenceViewSet,  basename='attendence')
router.register(r'shifts', ShiftViewSet,  basename='shifts')
router.register(r'employees', EmployeeViewSet,  basename='employees')
router.register(r'deductions', SalaryDeductionViewSet, basename='deductions')

urlpatterns = [
    path('',include(router.urls)),
]