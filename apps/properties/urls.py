from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'buildings', views.BuildingViewSet, basename='building')
router.register(r'units', views.PropertyViewSet, basename='property')

app_name = 'properties'

urlpatterns = [
    path('', include(router.urls)),
]
