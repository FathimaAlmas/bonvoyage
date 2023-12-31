# Generated by Django 4.2.3 on 2023-09-20 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('explore', '0012_remove_booking_hotel_remove_booking_package_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='hotel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='explore.hotel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='package',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='explore.packages'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='packages',
            name='package_id',
            field=models.PositiveIntegerField(blank=True, null=True, unique=True),
        ),
    ]
