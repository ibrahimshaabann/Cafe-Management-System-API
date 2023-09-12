from django.shortcuts import render
from rest_framework import viewsets
from human_resources.models import Customer, Employee, Shift, Attendence, SalaryDeduction
from .serializers import CustomerSerializer, ShiftSerializer, EmployeeSerializer, AttendanceSerializer, SalaryDeductionSerializer
from rest_framework.authentication import BasicAuthentication


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = [BasicAuthentication]
    # permission_classes = None
    # filter_backends = None
    # ordering_fields = None


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [BasicAuthentication]
    # permission_classes = None
    # filter_backends = None
    # ordering_fields = None

class ShiftViewSet(viewsets.ModelViewSet):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    authentication_classes = [BasicAuthentication]
    # permission_classes = None
    # filter_backends = None
    # ordering_fields = None


class AttendenceViewSet(viewsets.ModelViewSet):
    queryset = Attendence.objects.all()
    serializer_class = AttendanceSerializer
    authentication_classes = [BasicAuthentication]
    # permission_classes = None
    # filter_backends = None
    # ordering_fields = None


class SalaryDeductionViewSet(viewsets.ModelViewSet):
    queryset = SalaryDeduction.objects.all()
    serializer_class = SalaryDeductionSerializer
    authentication_classes = [BasicAuthentication]
    # permission_classes = None
    # filter_backends = None
    # ordering_fields = None
    