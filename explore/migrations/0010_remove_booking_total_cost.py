# Generated by Django 4.2.3 on 2023-09-19 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('explore', '0009_booking_total_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='total_cost',
        ),
    ]
