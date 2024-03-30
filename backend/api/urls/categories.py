from django.urls import path
from api.views.category_views import *  # Assuming your view is in 'api.views'

urlpatterns = [
    
    path('',Categories.as_view()),
    path('<slug:category_name>/products/', CategoryProductsAPIView.as_view(), name='category_products_api'),
]
