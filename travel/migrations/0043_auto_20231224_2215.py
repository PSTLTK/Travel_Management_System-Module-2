# Generated by Django 2.2 on 2023-12-24 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0042_auto_20231224_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='destinationmodel',
            name='adult_per_day',
            field=models.IntegerField(default=15000),
        ),
        migrations.AddField(
            model_name='destinationmodel',
            name='child_per_day',
            field=models.IntegerField(default=10000),
        ),
    ]
