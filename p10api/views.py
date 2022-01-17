from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.
class P10StatusViewSet(viewsets.ModelViewSet):
    queryset = P10Status.objects.all()
    serializer_class = P10StatusSerializer
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs) 
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    