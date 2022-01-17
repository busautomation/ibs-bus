from django.urls import path,include
from rest_framework import routers
from . import views
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()
routers.register('BusStatusApi', views.BusSatusDataViewSet,basename='BusStatusApi')
routers.register('SensorDataApi', views.SensorDataViewSet,basename='SensorDataApi')
routers.register('BusContactApi', views.BusContactViewSet,basename='BusContactApi')


urlpatterns = [
  path('',include(routers.urls)),
]
