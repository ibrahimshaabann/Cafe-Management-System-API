# Generated by Django 4.2.5 on 2023-09-16 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('human_resources', '0006_alter_shift_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attendence',
            options={'ordering': ['-id'], 'verbose_name_plural': 'الحضور والانصراف'},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ['-id'], 'verbose_name_plural': 'الموظف'},
        ),
    ]
