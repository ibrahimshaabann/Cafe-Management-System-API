# Generated by Django 4.2.5 on 2023-09-16 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_alter_order_customer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-id'], 'verbose_name_plural': 'الاوردرات'},
        ),
        migrations.AlterField(
            model_name='order',
            name='date_time',
            field=models.DateTimeField(auto_now=True, verbose_name='وقت الاوردر'),
        ),
    ]
