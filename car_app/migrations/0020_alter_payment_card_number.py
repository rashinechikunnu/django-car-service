# Generated by Django 5.0.6 on 2024-07-10 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0019_alter_create_work_name_manager_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='card_number',
            field=models.PositiveIntegerField(max_length=16),
        ),
    ]
