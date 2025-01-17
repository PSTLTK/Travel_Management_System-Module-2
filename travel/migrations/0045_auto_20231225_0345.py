# Generated by Django 2.2 on 2023-12-24 21:15

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0044_auto_20231224_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingmodel',
            name='b_code',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='bookingmodel',
            name='b_date',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='bookingmodel',
            name='b_email',
            field=models.EmailField(default=None, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='bookingmodel',
            name='b_name',
            field=models.CharField(max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='bookingmodel',
            name='b_phone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='bookingmodel',
            name='b_plan',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='bookingmodel',
            name='b_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bookingmodel',
            name='booked_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='bookingmodel',
            name='duration',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='bookingmodel',
            name='total_cost',
            field=models.BigIntegerField(default=None),
        ),
        migrations.AddField(
            model_name='bookingmodel',
            name='travel',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='travel.DestinationModel'),
        ),
        migrations.AlterField(
            model_name='bookingmodel',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
