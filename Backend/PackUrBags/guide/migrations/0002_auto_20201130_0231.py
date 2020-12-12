# Generated by Django 3.0.5 on 2020-11-30 02:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guidedata',
            name='last_booking_end_date',
            field=models.DateField(blank=True, default=datetime.datetime.today),
        ),
        migrations.AddField(
            model_name='guidedata',
            name='last_booking_start_date',
            field=models.DateField(blank=True, default=datetime.datetime.today),
        ),
    ]