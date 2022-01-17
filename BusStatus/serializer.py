from rest_framework import serializers
from .models import BusSatusData, SensorData, BusContact

class BusSatusDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusSatusData
        fields = '__all__'
class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = '__all__'
class BusContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusContact
        fields = '__all__'
        

