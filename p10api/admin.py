from django.contrib import admin
from .models import P10Status
# Register your models here.
class P10StatusAdmin(admin.ModelAdmin):
    list_display = ('device_name', 'device_message', 'device_brightness', 'device_scrolling_speed')
admin.site.register(P10Status, P10StatusAdmin)