from rest_framework import serializers
from django.db import models
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken, TokenError
from restaurants.models import Direction, Restaurant
from django.utils.text import gettext_lazy as _


class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = [
            "id",
            "city",
            "pc",
            "street",
            "int_number",
            "ext_number",
            "state",
            "location",
        ]


class RestaurantSerializer(serializers.ModelSerializer):
    direction = DirectionSerializer()

    class Meta:
        model = Restaurant
        fields = [
            "id",
            "name",
            "schedule_open",
            "schedule_close",
            "direction",
            "phone_number",
            "restaurant_type",

        ]


class RefreshTokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    # access = serializers.CharField()

    default_error_messages = {
        'bad_token': _('Token is invalid or expired')
    }

    def validate(self, attrs):
        print(attrs)
        self.refresh_token = attrs['refresh']
        # self.access_token = attrs['access']
        return attrs

    def save(self, **kwargs):
        try:
            # AccessToken(self.access_token).blacklist()
            RefreshToken(self.refresh_token).blacklist()
        except TokenError:
            self.fail('bad_token')
