from rest_framework.routers import DefaultRouter
from alcaldias.views import AlcaldiaViewSet


router = DefaultRouter() 
router.register('alcaldia', AlcaldiaViewSet, basename='alcaldia')

urlpatterns = []

urlpatterns += router.urls