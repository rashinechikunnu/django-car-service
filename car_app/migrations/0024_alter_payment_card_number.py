# Generated by Django 5.0.6 on 2024-07-10 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0023_alter_payment_card_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='card_number',
            field=models.CharField(max_length=16),
        ),
    ]
