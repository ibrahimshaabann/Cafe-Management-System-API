# Generated by Django 4.2.5 on 2023-09-12 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('human_resources', '0005_merge_20230912_1844'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shift',
            options={'ordering': ['-id'], 'verbose_name_plural': 'الشيفت'},
        ),
    ]