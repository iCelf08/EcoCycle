from rest_framework import viewsets
from django.contrib.auth import get_user_model
from .models import Trash, POI, Ramassage
from .serializers import UserSerializer, TrashSerializer, POISerializer, RamassageSerializer

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TrashViewSet(viewsets.ModelViewSet):
    queryset = Trash.objects.all()
    serializer_class = TrashSerializer

class POIViewSet(viewsets.ModelViewSet):
    queryset = POI.objects.all()
    serializer_class = POISerializer

class RamassageViewSet(viewsets.ModelViewSet):
    queryset = Ramassage.objects.all()
    serializer_class = RamassageSerializer
