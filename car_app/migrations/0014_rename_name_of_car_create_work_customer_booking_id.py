# Generated by Django 5.0.6 on 2024-07-03 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0013_alter_create_work_work_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='create_work',
            old_name='name_of_car',
            new_name='customer_booking_id',
        ),
    ]
