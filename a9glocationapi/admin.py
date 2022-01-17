from django.contrib import admin
from .models import LocationData
# Register your models here.
class LocationDataAdmin(admin.ModelAdmin):
    list_display = ('device_name', 'latitude', 'longitude')
admin.site.register(LocationData, LocationDataAdmin)
