from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TrashViewSet, RamassageViewSet

router = DefaultRouter()
router.register(r'Users', UserViewSet)
router.register(r'trash', TrashViewSet)
router.register(r'ramassage', RamassageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
