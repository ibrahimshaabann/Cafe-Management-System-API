from django.contrib import admin
from human_resources.models import Customer, Employee, SalaryDeduction, Shift, Attendence

admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(SalaryDeduction)
@admin.register(Attendence)
class AttendenceAdmin(admin.ModelAdmin):
    list_display = ('employee_attended','in_time','out_time','user_created_the_attendence')

@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ('login_time',
                    'logout_time',
                    'benefits',
                    'user',)



# Register your models here.
