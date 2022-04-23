from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
# Create your views here.

class ProductMaster(viewsets.ModelViewSet):
  queryset = Product.objects.all().order_by('id')
  serializer_class = ProductSerializer
