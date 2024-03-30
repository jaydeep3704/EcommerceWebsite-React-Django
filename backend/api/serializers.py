from rest_framework import serializers
from .models import *
class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    class Meta:
        model=Product
        fields='__all__'
    
class CategorySerializer(serializers.ModelSerializer):
    category_img = serializers.ImageField(use_url=True)
    class Meta:
        model=Category
        fields='__all__'