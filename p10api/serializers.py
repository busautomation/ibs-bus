from . models import P10Status
from rest_framework import serializers

class P10StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model=P10Status
        fields="__all__"
        # fields=('device_name', 'device_message', 'device_brightness', 'device_scrolling_speed')