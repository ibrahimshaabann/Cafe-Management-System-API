from django.contrib import admin
from human_resources.models import Customer, Employee, SalaryDeduction, Shift, Attendence

admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(SalaryDeduction)
admin.site.register(Shift)
admin.site.register(Attendence)


# Register your models here.
