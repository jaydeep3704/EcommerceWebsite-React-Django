from rest_framework import serializers
from .models import *


class ShippingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Shipping
        fields='__all__'     