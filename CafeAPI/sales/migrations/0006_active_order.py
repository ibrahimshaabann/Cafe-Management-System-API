# Generated by Django 4.2.5 on 2023-09-17 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0005_alter_menu_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='active_order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.order')),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.table')),
            ],
        ),
    ]
