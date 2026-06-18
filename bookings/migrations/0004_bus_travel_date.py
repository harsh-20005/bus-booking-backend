import datetime
from django.db import migrations, models


# This Django migration adds a new field called travel_date to the Bus model in your bookings app.



class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus', # 🔁 Modify the 'bus' model
            name='travel_date', # 🆕 Add new field 'travel_date'
            field=models.DateField(default=datetime.date(2025, 4, 24)), # 🗓 Default date used for applying existing records (only during migration)
            preserve_default=False,
        ),
    ]
