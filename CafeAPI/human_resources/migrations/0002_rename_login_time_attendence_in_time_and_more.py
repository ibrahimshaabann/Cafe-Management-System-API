# Generated by Django 4.2.5 on 2023-09-11 09:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('human_resources', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendence',
            old_name='login_time',
            new_name='in_time',
        ),
        migrations.RenameField(
            model_name='attendence',
            old_name='logout_time',
            new_name='out_time',
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=60, verbose_name='الاسم الاول')),
                ('lname', models.CharField(max_length=60, verbose_name='الاسم الثاني')),
                ('address', models.CharField(max_length=400, verbose_name='العنوان')),
                ('phone_no', models.CharField(max_length=11)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='المرتب')),
                ('deductions', models.DecimalField(decimal_places=2, default=0, max_digits=7, null=True, verbose_name='خصومات')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='اسم المستخدم')),
            ],
            options={
                'verbose_name_plural': 'الموظف',
            },
        ),
        migrations.AlterField(
            model_name='attendence',
            name='worker_attended',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='human_resources.employee', verbose_name='الموظف'),
        ),
        migrations.AlterField(
            model_name='salarydeduction',
            name='worker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SalaryDeduction', to='human_resources.employee', verbose_name='الموظف'),
        ),
        migrations.DeleteModel(
            name='Workers',
        ),
    ]
