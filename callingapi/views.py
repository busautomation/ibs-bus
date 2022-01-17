from django.shortcuts import render
from django.http import HttpResponse
from .models import CallingList
from .serializers import CallingListSerializer
from rest_framework.response import Response
from rest_framework import viewsets


# Create your views here.
class CallingListViewSet(viewsets.ModelViewSet):
    queryset = CallingList.objects.all()
    serializer_class = CallingListSerializer
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    