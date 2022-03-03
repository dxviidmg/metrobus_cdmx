from rest_framework.routers import DefaultRouter
from alcaldias.views import AlcaldiaViewSet, EstadoViewSet


router = DefaultRouter() 
router.register('estado', EstadoViewSet, basename='estado')
router.register('alcaldia', AlcaldiaViewSet, basename='alcaldia')

urlpatterns = []

urlpatterns += router.urls