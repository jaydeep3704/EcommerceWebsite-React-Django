from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND
from api.models import Category
from api.serializers import *



class Categories(ListAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
  
    lookup_field='slug'
    
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    



class CategoryProductsAPIView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        category = Category.objects.get(slug=category_name)
        return Product.objects.filter(category=category)

    



