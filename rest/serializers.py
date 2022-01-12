from django.db import models
from django.db.models import fields
from rest.models import Products, Seller, Users
from rest_framework import serializers


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
        
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['email', 'password']
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['name', 'price', 'user']
        
class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'        
