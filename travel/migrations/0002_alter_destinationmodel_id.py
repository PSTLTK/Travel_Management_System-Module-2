# Generated by Django 4.1 on 2023-11-30 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destinationmodel',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
