# from django.shortcuts import render
# from rest_framework.generics import *
# from main.serializers import *
# from main.models import *
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import filters

# class CategoryCreateListView(ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

# class CategoryRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     lookup_field = "pk"

# class BrandCreateListView(ListCreateAPIView):
#     queryset = Brand.objects.all()
#     serializer_class = BrandSerializer

# class BrandRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
#     queryset = Brand.objects.all()
#     serializer_class = BrandSerializer
#     lookup_field = "pk"

# class ProductCreateListView(ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
    
# class ProductRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = 'pk'



import django_filters
from django.shortcuts import render
from rest_framework.generics import *
from main.serializers import *
from main.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters

class CategoryCreateListView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.all()
        name = self.request.query_params.get("name")
        if name is not None:
               return Category.objects.filter(title__icontains=name) 
        return queryset

class CategoryRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "pk"

class BrandCreateListView(ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    def get_queryset(self):
        queryset = Brand.objects.all()
        name = self.request.query_params.get("name")
        if name is not None:
               return Brand.objects.filter(title__icontains=name) 
        return queryset

class BrandRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    lookup_field = "pk"

class ProductCreateListView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        queryset = Product.objects.all()
        name = self.request.query_params.get("name")
        if name is not None:
               return Product.objects.filter(title__icontains=name) 
        return queryset

class ProductRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
