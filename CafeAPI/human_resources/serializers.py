from rest_framework import serializers
from .models import Attendence, Customer, Employee, SalaryDeduction, Shift

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'
    

class CustomerSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        """
            Here, i used this method to check the json object data sent
            from via the url
        """
        print("#"*10 + "PUT OR PATCH json object data")
        print(validated_data)
        return super().update(instance, validated_data)
    
    
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
        fields = ['employee_attended', 'in_time', 'out_time', 'user_created_the_attendence']


class SalaryDeductionSerializer(serializers.ModelSerializer):

    class Meta:
        model = SalaryDeduction
        fields = ['employee', 'amount', 'description']
    