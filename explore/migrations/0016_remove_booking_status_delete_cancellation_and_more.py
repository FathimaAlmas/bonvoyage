# Generated by Django 4.2.3 on 2023-10-26 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explore', '0015_booking_status_cancellation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='status',
        ),
        migrations.DeleteModel(
            name='Cancellation',
        ),
        migrations.AddField(
            model_name='booking',
            name='STATUS',
            field=models.BooleanField(default=False),
        ),
    ]
