# Generated by Django 5.0 on 2024-01-28 15:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_appointment_status2'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
