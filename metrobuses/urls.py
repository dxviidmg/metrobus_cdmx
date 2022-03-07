
from rest_framework.routers import DefaultRouter
from metrobuses.views import MetrobusViewSet


router = DefaultRouter() 
router.register('metrobus', MetrobusViewSet, basename='metrobus')

urlpatterns = []

urlpatterns += router.urls