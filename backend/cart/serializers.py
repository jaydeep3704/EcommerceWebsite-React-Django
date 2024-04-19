from rest_framework import serializers
from .models import *
from api.serializers import *
from users.serializers import *


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields='__all__'
        

class CartItemsSerializer(serializers.ModelSerializer):
    cart=CartSerializer()
    product=ProductSerializer()
    class Meta:
        model=CartItems
        fields='__all__'     
        
        
class OrderSerializer(serializers.ModelSerializer):
    cart=CartSerializer()
 
    class Meta:
        model=Orders
        fields='__all__'
        
