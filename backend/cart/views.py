from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *


class CartView(APIView):
    permission_classes=[IsAuthenticated]
    
    def get(self,request):
        user=request.user
        cart=Cart.objects.filter(user=user,ordered=False).first()
        queryset=CartItems.objects.filter(cart=cart)
      
        serializer=CartItemsSerializer(queryset,many=True)
        
        return Response(serializer.data)
    
    def post(self,request):
        data=request.data
        user=request.user
        cart,_=Cart.objects.get_or_create(user=user,ordered=False)
        product=Product.objects.get(id=data.get('id'))
        price=product.price
        quantity=data.get('quantity')
        cart_items=CartItems(cart=cart,user=user,product=product,price=price,quantity=quantity)
        cart_items.save()
        cart_items=CartItems.objects.filter(user=user,cart=cart)
        total_price=0
        for items in cart_items:
            total_price+=items.price
            
        cart.total_price=total_price
        cart.save()
        print(cart_items)
        return Response({'success':'Items added to your cart'})
    
    def delete(self,request):
        data=request.data
        user=request.user
        id=data.get('id')
        cart=Cart.objects.filter(user=user,ordered=False).first()
        cart_item=CartItems.objects.filter(cart=cart,id=id)
        cart_item.delete()
        
        cart_items=CartItems.objects.filter(user=user,cart=cart)
        total_price=0
        for items in cart_items:
            total_price+=items.price
            
        cart.total_price=total_price
        cart.save()
        
        queryset=CartItems.objects.filter(cart=cart)
        serializer=CartItemsSerializer(queryset,many=True)
        return Response(serializer.data)
    
    def put(self,request):
        data=request.data
        user=request.user
        
        cart_item=CartItems.objects.filter(id=data.get('id')).first()
        cart_item.quantity=data.get('quantity')
        cart_item.save()
        
        cart=Cart.objects.filter(user=user,ordered=False).first()
        cart_items=CartItems.objects.filter(cart=cart,user=user)
         
        total_price=0
        for items in cart_items:
            total_price+=items.price
            
        cart.total_price=total_price
        cart.save()
        
        
        
        
        return Response({'sucess':'Items Updated'})
    