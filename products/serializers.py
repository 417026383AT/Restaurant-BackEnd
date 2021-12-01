from django.db.models import fields
from rest_framework import serializers
from products.models import Products
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken, TokenError


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = [
            "id",
            "name",
            "price",
            "description",
            "image",
        ]


# class RefreshTokenSerializer(serializers.Serializer):
#     refresh = serializers.CharField()
#     # access = serializers.CharField()

#     default_error_messages = {
#         'bad_token': _('Token is invalid or expired')
#     }

#     def validate(self, attrs):
#         print(attrs)
#         self.refresh_token = attrs['refresh']
#         # self.access_token = attrs['access']
#         return attrs

#     def save(self, **kwargs):
#         try:
#             # AccessToken(self.access_token).blacklist()
#             RefreshToken(self.refresh_token).blacklist()
#         except TokenError:
#             self.fail('bad_token')
