from django.shortcuts import render
from django.http import HttpResponse
from .models import LocationData
from .serializers import LocationDataSerializer
from rest_framework.response import Response
from rest_framework import viewsets
# Create your views here.

class LocationDataViewSet(viewsets.ModelViewSet):
    queryset = LocationData.objects.all()
    serializer_class = LocationDataSerializer
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
