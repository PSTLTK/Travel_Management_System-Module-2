# Generated by Django 2.2 on 2023-12-19 01:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('travel', '0030_delete_bookingmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
