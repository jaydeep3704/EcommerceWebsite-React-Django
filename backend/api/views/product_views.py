from django.shortcuts import render
from api.serializers import *
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView
from rest_framework.filters import SearchFilter

# Create your views here.

class ProductListAndCreate(ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    filter_backends=[SearchFilter]
    search_fields=['product_name','price']
    
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class ProductReadUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self,request,*args,**kwargs):
        return self.delete(request,*args,**kwargs)    
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    

    
    
    