# Generated by Django 2.2 on 2023-12-24 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0043_auto_20231224_2215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookingmodel',
            name='booked_at',
        ),
        migrations.RemoveField(
            model_name='bookingmodel',
            name='night',
        ),
        migrations.RemoveField(
            model_name='bookingmodel',
            name='number_of_person',
        ),
        migrations.RemoveField(
            model_name='bookingmodel',
            name='travel',
        ),
        migrations.AlterField(
            model_name='bookingmodel',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='bookingmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='destinationmodel',
            name='flight_price',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='destinationmodel',
            name='food_price',
            field=models.IntegerField(default=None),
        ),
    ]
