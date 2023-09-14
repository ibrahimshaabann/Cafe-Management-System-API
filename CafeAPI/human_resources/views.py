from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from human_resources.models import Customer, Employee, Shift, Attendence, SalaryDeduction
from .serializers import CustomerSerializer, ShiftSerializer, EmployeeSerializer, AttendanceSerializer, SalaryDeductionSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import CustomerAccessPermission, ShiftOrAttendencePermission, SalOrEmpAccessPermission


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, CustomerAccessPermission]
    # filter_backends = None
    # ordering_fields = None


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, SalOrEmpAccessPermission]
    # filter_backends = None
    # ordering_fields = None

class ShiftViewSet(ModelViewSet):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, ShiftOrAttendencePermission]   
    # filter_backends = None
    # ordering_fields = None


class AttendenceViewSet(ModelViewSet):
    queryset = Attendence.objects.all()
    serializer_class = AttendanceSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, ShiftOrAttendencePermission]   
    # filter_backends = None
    # ordering_fields = None


class SalaryDeductionViewSet(ModelViewSet):
    queryset = SalaryDeduction.objects.all()
    serializer_class = SalaryDeductionSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, SalOrEmpAccessPermission]
    # filter_backends = None
    # ordering_fields = None
    