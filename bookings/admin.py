from django.contrib import admin
from .models import Bus, Seat, Booking


# Customize the admin interface for the Bus model
class BusAdmin(admin.ModelAdmin):
    # Columns to display in the admin list view for Bus
    list_display = ('bus_name', 'number', 'origin', 'destination', 'start_time', 'reach_time', 'no_of_seats', 'price')

class SeatAdmin(admin.ModelAdmin):
    # Customize the admin interface for the Seat model
    list_display = ('seat_number', 'bus', 'is_booked')

class BookingAdmin(admin.ModelAdmin):
    # Customize the admin interface for the Booking model
    list_display = ('user', 'bus', 'seat', 'booking_time', 'origin','price')

admin.site.register(Bus, BusAdmin)
admin.site.register(Seat, SeatAdmin)
admin.site.register(Booking, BookingAdmin)
