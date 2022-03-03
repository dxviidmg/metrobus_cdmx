from rest_framework.routers import DefaultRouter
from alcaldias.views import TownHallViewSet, StateViewSet


router = DefaultRouter() 
router.register('estado', StateViewSet, basename='estado')
router.register('alcaldia', TownHallViewSet, basename='alcaldia')

urlpatterns = []

urlpatterns += router.urls