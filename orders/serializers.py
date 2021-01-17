from rest_framework import serializers 
from orders.models import BaseOrder
 
 
class OrderSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = BaseOrder
        fields = ('id',
                  'customer',
                  'date_created',
                  'total_cost',
                  
                  )