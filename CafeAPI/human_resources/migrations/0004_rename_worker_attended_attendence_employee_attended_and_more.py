# Generated by Django 4.2.5 on 2023-09-11 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('human_resources', '0003_customer_alter_salarydeduction_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendence',
            old_name='worker_attended',
            new_name='employee_attended',
        ),
        migrations.RenameField(
            model_name='salarydeduction',
            old_name='worker',
            new_name='employee',
        ),
    ]