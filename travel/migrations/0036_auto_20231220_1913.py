# Generated by Django 2.2 on 2023-12-20 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0035_auto_20231220_1912'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedbackmodel',
            old_name='fb_detail',
            new_name='fbdetail',
        ),
    ]
