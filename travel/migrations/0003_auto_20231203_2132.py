# Generated by Django 2.2 on 2023-12-03 15:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0002_alter_destinationmodel_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('blog', models.CharField(max_length=100)),
                ('description', models.TextField(default=None)),
                ('image', models.ImageField(default=None, upload_to='')),
                ('time', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.AddField(
            model_name='destinationmodel',
            name='time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
