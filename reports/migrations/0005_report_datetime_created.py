# Generated by Django 5.1.1 on 2024-10-01 14:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0004_alter_report_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='datetime_created',
            field=models.DateTimeField(auto_created=True, auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
