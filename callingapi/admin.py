from django.contrib import admin
from .models import CallingList
# Register your models here.

class CallingListAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'callingstatus')
admin.site.register(CallingList, CallingListAdmin)
