from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    slug = serializers.CharField()
    image = serializers.ImageField()
    description = serializers.TextField()
    price = serializers.DecimalField()
    available = serializers.BooleanField(default=True)
    created = serializers.DateTimeField()
    uploaded = serializers.DateTimeField()










# class ProductModel:
#     def __init__(self, name, description):
#         self.name = name
#         self.description = description
        
        
# class ProductSerializer(serializers.ModelSerializer):
#     name = serializers.CharField(max_length=230)
#     description = serializers.CharField()
    
    
# def encode():
#     model = ProductModel()
#     model_sr = ProductSerializer(model)
    