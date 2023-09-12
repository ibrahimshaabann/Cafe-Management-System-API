from rest_framework import serializers
from .models import Attendence, Customer, Employee, SalaryDeduction, Shift

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'
    

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'



class ShiftSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shift
        fields = ['login_time', 'logout_time', 'user']



class AttendanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attendence
        fields = ['employee_attendedl', 'in_time', 'out_time', 'user_created_the_attendence']


class SalaryDeductionSerializer(serializers.ModelSerializer):

    class Meta:
        model = SalaryDeduction
        fields = ['employee', 'amount', 'description']
    