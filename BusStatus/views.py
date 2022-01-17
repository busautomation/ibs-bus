from django.shortcuts import render
from .models import BusSatusData, SensorData, BusContact
from .serializer import BusSatusDataSerializer, SensorDataSerializer, BusContactSerializer
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.
class BusSatusDataViewSet(viewsets.ModelViewSet):
    queryset = BusSatusData.objects.all()
    serializer_class = BusSatusDataSerializer
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

class SensorDataViewSet(viewsets.ModelViewSet):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    def partial_update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

class BusContactViewSet(viewsets.ModelViewSet):
    queryset = BusContact.objects.all()
    serializer_class = BusContactSerializer
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    def partial_update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)