from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view

from orderItems.models import BaseOrderIetms
from orderItems.serializers import OrderItemsSerializer


# Create your views here.


@api_view(['POST','GET'])
def PostOrderItems(request):
    # GET list of products, POST a new product, DELETE all products
    if request.method == 'GET':
        orderItems = BaseOrderIetms.objects.all()
        orderItems_serializer = OrderItemsSerializer(orderItems, many=True)
        return JsonResponse(orderItems_serializer.data, safe=False)
        # 'safe=False' for objects serialization
         
    if request.method == 'POST':
        orderItems_data = JSONParser().parse(request)
        orderItems_serializer = OrderItemsSerializer(data=orderItems_data)
        if orderItems_serializer.is_valid():
            orderItems_serializer.save()
            return JsonResponse(orderItems_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(orderItems_serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

 
 
