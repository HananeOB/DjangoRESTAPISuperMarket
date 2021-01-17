from rest_framework import serializers 
from product.models import BaseProduct
 
 
class ProductSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = BaseProduct
        fields = ('id',
                  'name',
                  'price',
                  'discounts',
                  'available_quantity'
                  #,'image'
                  )