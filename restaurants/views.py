from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from restaurants.models import *
from restaurants.serializers import *
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

from .serializers import *
from .models import *
from users.views import verify_token

# Create your views here.


class DirectionViewSet(ModelViewSet):
    queryset = Direction.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = DirectionSerializer


class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = RestaurantSerializer


class RestaurantView(APIView):
    def get(self, request):
        payload = verify_token(request)
        restaurant = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurant, many=True)
        return Response(serializer.data)


class LogoutView(GenericAPIView):
    serializer_class = RefreshTokenSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args):
        sz = self.get_serializer(data=request.data)
        sz.is_valid(raise_exception=True)
        sz.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
