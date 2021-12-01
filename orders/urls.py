from django.urls import path

from restaurants.views import DirectionViewSet, RestaurantViewSet
from django.urls import path, include
from rest_framework import routers
from .views import *


urlpatterns = [
    path('Orders', OrderViewSet.as_view({'get': 'list'})),
    path('OrderProducts', OrderProductsViewSet.as_view({'get': 'list'}))
]
