# Generated by Django 5.0.6 on 2024-06-28 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0006_rename_shedule_customer_booking_schedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_booking',
            name='number_plate',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='customer_booking',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
