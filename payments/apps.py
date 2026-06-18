from django.apps import AppConfig


class PaymentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'payments'


# So this line just ensures your payment app is active and Django will load its models, views, etc.