# Generated by Django 2.2 on 2023-12-26 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0046_auto_20231225_1314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destinationmodel',
            name='food_price',
        ),
    ]
