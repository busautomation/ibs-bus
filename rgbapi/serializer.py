from rest_framework import serializers
from .models import RGB,Dimmer

class RGBSerializer(serializers.ModelSerializer):
    class Meta:
        model = RGB
        fields ="__all__"

class DimmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dimmer
        fields ="__all__"