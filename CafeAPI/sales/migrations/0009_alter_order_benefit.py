# Generated by Django 4.2.5 on 2023-09-18 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('financials', '0003_alter_benefits_end_date'),
        ('sales', '0008_order_benefit_delete_active_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='benefit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='financials.benefits', verbose_name='رقم فتره الربح'),
        ),
    ]
