from django.contrib import admin
from .models import Guest, Business, Booking

# Register your models here.
admin.site.register(Guest)
admin.site.register(Business)
admin.site.register(Booking)
