from django.urls import path
from .views import *

urlpatterns=[
    path('orders/',OrderAPI.as_view()),
    path('cart/',CartView.as_view()),
]