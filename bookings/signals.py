
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Bus, Seat

# This Django signal handler performs a crucial function in a
# bus seat booking system by automatically creating all seats for a newly created bus.

# post_save: A signal that gets sent after a model's save() method completes
# receiver: Decorator that connects a signal to a function

@receiver(post_save, sender=Bus)
def create_seats_for_bus(sender, instance, created, **kwargs):
    if created:
        for i in range(1, instance.no_of_seats +1):
            Seat.objects.create(bus=instance, seat_number= f"S{i}")