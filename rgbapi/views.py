from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import RGB,Dimmer
from .serializer import RGBSerializer,DimmerSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.
class RGBViewSet(viewsets.ModelViewSet):
    queryset = RGB.objects.all()
    serializer_class = RGBSerializer
    #update the array i one go
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
class DimmerViewSet(viewsets.ModelViewSet):
    queryset = Dimmer.objects.all()
    serializer_class = DimmerSerializer
    #update the array i one go
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)



