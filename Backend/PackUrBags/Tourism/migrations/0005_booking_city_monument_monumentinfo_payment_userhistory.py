# Generated by Django 3.0.4 on 2020-10-28 12:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('guide', '0001_initial'),
        ('tourism', '0004_auto_20201028_1257'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now=True, verbose_name='Booked at ')),
                ('guide_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='b_guide_email', to='guide.GuideData')),
                ('user_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='b_user_email', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('city_id', models.AutoField(primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('pin_code', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Monument',
            fields=[
                ('monument_id', models.AutoField(primary_key=True, serialize=False)),
                ('monument_name', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('basic_info', models.TextField()),
                ('pin_code', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='UserHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode_of_payment', models.CharField(choices=[('1', 'Debit/Credit card'), ('2', 'UPI'), ('3', 'Cash'), ('4', 'Net banking')], default='2', max_length=1)),
                ('mode_of_travel', models.IntegerField(choices=[(1, 'Bus'), (2, 'Flight'), (3, 'Train'), (4, 'Cab'), (5, 'Ship')], default=1)),
                ('travel_amount', models.IntegerField()),
                ('restaurant', models.CharField(max_length=100)),
                ('food_amount', models.IntegerField()),
                ('lodge', models.CharField(max_length=100)),
                ('stay_amount', models.IntegerField()),
                ('timestamp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='u_timestamp', to='tourism.Booking')),
                ('user_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='u_user_email', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('mode_of_payment', models.CharField(choices=[('1', 'Debit/Credit card'), ('2', 'UPI'), ('3', 'Cash'), ('4', 'Net banking')], default='2', max_length=1)),
                ('timestamp', models.DateTimeField(auto_now=True, verbose_name='Booked at ')),
                ('booking_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='p_booking_id', to='tourism.Booking')),
                ('guide_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='p_guide_email', to='guide.GuideData')),
                ('user_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='p_user_email', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MonumentInfo',
            fields=[
                ('monument_info_id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=100)),
                ('info', models.TextField()),
                ('monument_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tourism.Monument')),
            ],
        ),
    ]
