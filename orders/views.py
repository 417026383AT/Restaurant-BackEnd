from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
from users.views import verify_token
# Create your views here.


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer


class OrderProductsViewSet(ModelViewSet):
    queryset = OrderProducts.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = OrderProductsSerializer
