from django.urls import path

from products.views import ProductsView, ProductsViewSet
from django.urls import path, include
from rest_framework import routers
from users.views import *
# import everything from views

# define the router
router = routers.DefaultRouter()

# define the router path and viewset to be used
router.register(r'', ProductsViewSet)

# URLS
urlpatterns = [
    path('', include(router.urls)),
    path('view', ProductsView.as_view()),
    path('logout', LogoutView.as_view(), name='auth_logout'),
]
urlpatterns += [
    path('Products', ProductsViewSet.as_view({'get': 'list'}))
]
