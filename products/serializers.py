from rest_framework import serializers

from products.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    products = serializers.StringRelatedField(many=True)
    class Meta:
        model = Category
        fields = ['name','description','products']


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product 
        fields = ['name','description','old_price','price','slug']