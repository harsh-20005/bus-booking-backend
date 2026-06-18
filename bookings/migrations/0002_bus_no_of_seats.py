from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
        # This ensures that the first migration (model creation) runs before this one
    ]

    # ➕ Add a new field to the Bus model
    operations = [
        migrations.AddField(
            model_name='bus',   # 📌 The model being updated is 'Bus'
            name='no_of_seats',  # 🆕 New field name: no_of_seats
            field=models.PositiveBigIntegerField(default=20),  
            # ✅ Field type: only positive integers, large size (up to 9 quintillion)
            # ✅ Default value: 20 (used when adding to existing records)
            preserve_default=False,  # 🚫 Don't preserve the default in model after migration
        ),
    ]
