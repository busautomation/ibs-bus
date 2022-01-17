from django.urls import path,include
from rest_framework import routers
from . import views
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()
routers.register('rgb', views.RGBViewSet,basename='rgb')
routers.register('dimmer', views.DimmerViewSet,basename='dimmer')



urlpatterns = [
  path('',include(routers.urls)),
]
