from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Tags, Category, Product
from .serializers import CategorySerializer, TagsSerializer, ProductSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def list_product(request):
    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        print(serializer.data)

        return Response(serializer.data)
    
@api_view(['GET'])
def product_dateil(request, id):
    if request.method == 'GET':
        product = get_object_or_404(Product, id=id)
        serializer = ProductSerializer(product)

        return Response(serializer.data)


@api_view(['GET'])
def list_category(request):
    if request.method == 'GET':
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)

        return Response(serializer.data)
    
@api_view(['GET'])
def category_dateil(request, id):
    if request.method == 'GET':
        category = get_object_or_404(Category, id=id)
        serializer = CategorySerializer(category)

        return Response(serializer.data)
    

@api_view(['GET'])
def list_tags(request):
    if request.method == 'GET':
        tags = Tags.objects.all()
        serializer = TagsSerializer(tags, many=True)

        return Response(serializer.data)
    
@api_view(['GET'])
def tags_detail(request, id):
    if request.method == 'GET':
        tags = get_object_or_404(Tags, id=id)
        serializer = TagsSerializer(tags)

        return Response(serializer.data)