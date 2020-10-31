# Generated by Django 3.0.5 on 2020-10-31 23:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('guide', '0004_delete_place'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now=True, verbose_name='Booked at ')),
                ('guide_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='b_guide_email', to='guide.GuideData')),
                ('user_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='b_user_email', to=settings.AUTH_USER_MODEL)),
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
                ('timestamp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='u_timestamp', to='Tourism.Booking')),
                ('user_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='u_user_email', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('mode_of_payment', models.CharField(choices=[('1', 'Debit/Credit card'), ('2', 'UPI'), ('3', 'Cash'), ('4', 'Net banking')], default='2', max_length=1)),
                ('timestamp', models.DateTimeField(auto_now=True, verbose_name='Booked at ')),
                ('booking_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='p_booking_id', to='Tourism.Booking')),
                ('guide_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='p_guide_email', to='guide.GuideData')),
                ('user_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='p_user_email', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
