# Generated by Django 3.0.4 on 2020-10-28 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0003_auto_20201028_0819'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='guide_email',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='user_email',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.RemoveField(
            model_name='monumentinfo',
            name='monument_name',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='booking_id',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='guide_email',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='user_email',
        ),
        migrations.RemoveField(
            model_name='userhistory',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='userhistory',
            name='user_email',
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.DeleteModel(
            name='Monument',
        ),
        migrations.DeleteModel(
            name='MonumentInfo',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.DeleteModel(
            name='UserHistory',
        ),
    ]
