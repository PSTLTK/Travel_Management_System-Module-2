# Generated by Django 2.2 on 2023-12-10 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0015_delete_blogmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='registerationmodel',
            name='profile',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]