from rest_framework.viewsets import ModelViewSet
from .models import Product, Category
from .searilizers import ProductSerializer, CategorySerializer

class Category_Vw(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class Product_Vw(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer