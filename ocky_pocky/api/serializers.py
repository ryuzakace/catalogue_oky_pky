from rest_framework import serializers

from ..models import Categories, SubCategories, Products

class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = ['category']

class SubCategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubCategories
        fields = ['sub_category']


class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = ['product']

