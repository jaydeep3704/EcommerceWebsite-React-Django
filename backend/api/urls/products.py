
from django.urls import path
from api.views.product_views import *



urlpatterns = [
 
path('',ProductListAndCreate.as_view()),
path('<int:pk>',ProductReadUpdateDelete.as_view()),
]
