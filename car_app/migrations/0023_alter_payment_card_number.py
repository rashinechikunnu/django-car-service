# Generated by Django 5.0.6 on 2024-07-10 10:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0022_alter_payment_card_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='card_number',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(16)]),
        ),
    ]
