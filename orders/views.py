from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view

from orders.models import BaseOrder
from orders.serializers import OrderSerializer


# Create your views here.


@api_view(['POST','GET'])
def PostOrders(request):
    # GET list of products, POST a new product, DELETE all products
    if request.method == 'GET':
        orders = BaseOrder.objects.all()
        orders_serializer = OrderSerializer(orders, many=True)
        return JsonResponse(orders_serializer.data, safe=False)
        # 'safe=False' for objects serialization
         
    if request.method == 'POST':
        orders_data = JSONParser().parse(request)
        orders_serializer = OrderSerializer(data=orders_data)
        if orders_serializer.is_valid():
            orders_serializer.save()
            return JsonResponse(orders_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(orders_serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

 
 
