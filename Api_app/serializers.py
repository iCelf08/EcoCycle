from rest_framework import serializers
from django.contrib.auth.models import User
from .models import User, Trash, Ramassage

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    is_enterprise = serializers.BooleanField()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password', 'is_enterprise')
        
class EnterpriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_enterprise']
        

class TrashSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trash
        fields = ('id', 'type', 'price_per_kilo', 'co2')

class RamassageSerializer(serializers.ModelSerializer):
    co2_saved = serializers.ReadOnlyField()
    balance = serializers.ReadOnlyField()

    class Meta:
        model = Ramassage
        fields = ['id', 'user', 'trash_type', 'weight', 'collection_date', 'co2_saved', 'balance']

