from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .serializer import CategorySerializer, SupplierSerializer, ProductSerializer


from core_apps.Product.models import Product, Category, Supplier
from .serializer import ProductSerializer

# Create your views here.


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SupplierViewSet(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
