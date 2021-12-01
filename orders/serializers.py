from django.db.models import fields
from rest_framework import serializers
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken, TokenError
from .models import Order, OrderProducts, Status
from restaurants.serializers import RestaurantSerializer
from users.serializers import UserSerializer
from products.serializers import ProductsSerializer


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [
            "id",
            "code",
            "description",
        ]


class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    restaurant = RestaurantSerializer()
    status = StatusSerializer()

    class Meta:
        model = Order
        fields = [
            "user",
            "time",
            "restaurant",
            "status",
            "products",
        ]


class OrderProductsSerializer(serializers.ModelSerializer):
    order = OrderSerializer
    product = ProductsSerializer

    class Meta:
        model = OrderProducts
        fields = [
            "order",
            "product",
            "quantity",
        ]
