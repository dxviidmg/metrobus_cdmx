
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from metrobuses.views import MetrobusViewSet


router = DefaultRouter() 
router.register('metrobus', MetrobusViewSet, basename='metrobus')

urlpatterns = []

urlpatterns += router.urls