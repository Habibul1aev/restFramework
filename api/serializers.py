from rest_framework.serializers import ModelSerializer
from framework.models import Tags, Category, Product

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TagsSerializer(ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'