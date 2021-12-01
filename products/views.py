from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from products.models import Products
from products.serializers import ProductsSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from users.views import verify_token
# Create your views here.


class ProductsViewSet(ModelViewSet):
    queryset = Products.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProductsSerializer


class ProductsView(APIView):
    def post(self, request):
        serializer = ProductsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self, request):
        payload = verify_token(request)
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)

    def put(self, request):
        pass

    def patch(self, request):
        pass

    def delete(self, request):
        pass
