# Generated by Django 4.2.5 on 2023-09-11 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('human_resources', '0002_rename_login_time_attendence_in_time_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=60, verbose_name='الاسم الاول')),
                ('lname', models.CharField(max_length=60, verbose_name='الاسم الثاني')),
                ('first_address', models.CharField(blank=True, max_length=400, null=True, verbose_name='العنوان الأول')),
                ('second_address', models.CharField(blank=True, max_length=400, null=True, verbose_name=' العنوان الثاني')),
                ('phone_no', models.CharField(max_length=11)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='salarydeduction',
            options={'get_latest_by': 'date', 'verbose_name_plural': 'خصومات المرتب'},
        ),
        migrations.AlterModelOptions(
            name='shift',
            options={'ordering': [-1], 'verbose_name_plural': 'الشيفت'},
        ),
        migrations.RemoveField(
            model_name='employee',
            name='address',
        ),
        migrations.AddField(
            model_name='employee',
            name='first_address',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='العنوان الأول'),
        ),
        migrations.AddField(
            model_name='employee',
            name='second_address',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name=' العنوان الثاني'),
        ),
    ]
