# Generated by Django 5.1.4 on 2025-01-01 07:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_alter_post_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2025, 1, 1, 11, 11, 44, 161888)),
        ),
    ]
