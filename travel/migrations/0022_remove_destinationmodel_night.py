# Generated by Django 2.2 on 2023-12-16 23:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0021_auto_20231216_2236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destinationmodel',
            name='night',
        ),
    ]
