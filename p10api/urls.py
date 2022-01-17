from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register("",views.P10StatusViewSet,basename="P10Api")


urlpatterns = [
    path("", include(router.urls)),
    
]
