# Generated by Django 4.0.1 on 2022-04-18 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_employee_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]
