from django.apps import AppConfig


class BookingsConfig(AppConfig):
    # This sets the default type of primary key for models in this app.
    # 'BigAutoField' means the primary key will be a big integer that auto-increments.
    default_auto_field = 'django.db.models.BigAutoField'
    
    # The name of the app this configuration applies to.
    name = 'bookings'

    def ready(self):
        # Import the signals module here so that Django registers signal handlers.
        # This avoids issues with signals not being connected if imported too early.
        import bookings.signals