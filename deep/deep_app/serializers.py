from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = '__all__'   # or ->  ['image','name','price','description','category']
