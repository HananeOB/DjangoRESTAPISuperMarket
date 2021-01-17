from rest_framework import serializers 
from orderItems.models import BaseOrderIetms
 
 
class OrderItemsSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = BaseOrderIetms
        fields = ( 
                  'order',
                  'product',
                  'quantity',
                  )