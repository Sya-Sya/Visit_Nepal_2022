from django.contrib import admin
from .models import Room, RoomCategory, Booking
# Register your models here.
admin.site.register(RoomCategory)
admin.site.register(Room)
admin.site.register(Booking)
