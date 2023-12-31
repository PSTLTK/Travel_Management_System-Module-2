# Generated by Django 2.2 on 2023-12-16 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0020_alter_destinationmodel_bus_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destinationmodel',
            name='bus_price',
        ),
        migrations.RemoveField(
            model_name='destinationmodel',
            name='train_price',
        ),
        migrations.AddField(
            model_name='destinationmodel',
            name='day',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='destinationmodel',
            name='night',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='destinationmodel',
            name='number_of_person',
            field=models.IntegerField(default=None),
        ),
        migrations.DeleteModel(
            name='UserTableModel',
        ),
    ]
