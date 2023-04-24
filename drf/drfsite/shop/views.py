from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import render
from .models import Product, Category, Order
from .serializers import ProductSerializer
from .models import APIView

from shop.models import Product


class ProductAPIView(APIView):
    def get(self, request):
        lst = Product.objects.all(). values()
        return Response({'posts': list(lst)})
    
    
          
          
          

# class ProductAPIView(generics.ListAPIView):
#     queryset =Product.objects.all()
#     serializer_class = ProductSerializer
    
    
    #get - отвечает за обработку get запроосов
    