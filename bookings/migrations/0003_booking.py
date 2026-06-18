import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


# You're looking at a Django migration file that creates a new model called Booking.
# This model is used to store bus ticket bookings made by users, connecting users to specific buses and seats.

class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_bus_no_of_seats'), # Must apply this migration first
        migrations.swappable_dependency(settings.AUTH_USER_MODEL), # Ensure User model exists
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',# 🎯 Model/table being created: Booking
            fields=[
                # Primary Key (auto-incrementing ID)
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                # 📅 Automatically stores the date & time when a booking is created
                ('booking_time', models.DateTimeField(auto_now_add=True)),
                # 🔗 ForeignKey to Bus model
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.bus')),
                ('seat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.seat')), # If seat is deleted, delete booking
                # 🔗 ForeignKey to User model (auth user)
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),# If user is deleted, delete booking
                # Use the currently active user model
            ],
        ),
    ]
