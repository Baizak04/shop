from rest_framework import generics
from django.shortcuts import render
from .models import Product, Category, Order
from .serializers import ProductSerializer

from shop.models import Product

class ProductAPIView(generics.ListAPIView):
    queryset =Product.objects.all()
    serializer_class = ProductSerializer
    