from rest_framework.routers import DefaultRouter
from alcaldias.views import TownHallViewSet, StateViewSet


router = DefaultRouter() 
router.register('estado', StateViewSet, basename='state')
router.register('alcaldia', TownHallViewSet, basename='townhall')

urlpatterns = []

urlpatterns += router.urls