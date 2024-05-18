from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Trash, POI, Ramassage

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    total_co2_saved = serializers.ReadOnlyField()
    total_balance = serializers.ReadOnlyField()
    
    class Meta:
        model = User
        fields = ['id', 'username', 'is_enterprise', 'total_co2_saved', 'total_balance']

class TrashSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trash
        fields = ['id', 'type', 'price_per_kilo', 'co2']

class POISerializer(serializers.ModelSerializer):
    class Meta:
        model = POI
        fields = ['id', 'name', 'address']

class RamassageSerializer(serializers.ModelSerializer):
    balance = serializers.ReadOnlyField()
    co2_saved = serializers.ReadOnlyField()
    
    class Meta:
        model = Ramassage
        fields = ['id', 'user', 'trash_type', 'poi', 'weight', 'collection_date', 'balance', 'co2_saved']
