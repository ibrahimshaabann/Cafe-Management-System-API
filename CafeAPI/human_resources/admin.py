from django.contrib import admin
from human_resources.models import Customer, Employee, SalaryDeduction, Shift, Attendence

admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(SalaryDeduction)
admin.site.register(Attendence)


@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ('login_time',
                    'logout_time',
                    'benefits',
                    'user',)



# Register your models here.
