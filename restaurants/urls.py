from django.urls import path

from restaurants.views import DirectionViewSet, RestaurantViewSet
from django.urls import path, include
from rest_framework import routers
from .views import *
# import everything from views

# define the router
router = routers.DefaultRouter()

# define the router path and viewset to be used
router.register(r'', RestaurantViewSet)
router.register(r'direction', DirectionViewSet)

# URLS
urlpatterns = [
    path('', include(router.urls)),
    path('view', RestaurantView.as_view()),
    path('logout', LogoutView.as_view(), name='auth_logout'),
]
urlpatterns += [
    path('Directions', DirectionViewSet.as_view({'get': 'list'})),
    path('Restaurants', RestaurantViewSet.as_view({'get': 'list'}))
]
