from django import urls
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

routers=DefaultRouter()
routers.register('',views.LocationDataViewSet)


urlpatterns = [
   path('',include(routers.urls)),
]
