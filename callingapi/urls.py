from django.urls import path,include
from rest_framework import routers
from . import views
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()
routers.register('', views.CallingListViewSet, basename='callinglist')


urlpatterns = [
    path('', include(routers.urls)),
]
