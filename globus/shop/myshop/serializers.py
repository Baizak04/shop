from .models import Category,Product
from rest_framework import serializers


class ProdructSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['category','name','slug','description','image','available','price','created','uploaded']

    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name','slug']

