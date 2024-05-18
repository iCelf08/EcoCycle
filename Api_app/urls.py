from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TrashViewSet, POIViewSet, RamassageViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'trash', TrashViewSet)
router.register(r'pois', POIViewSet)
router.register(r'ramassages', RamassageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]
