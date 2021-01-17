from django.urls import path, re_path
from orderItems import views

urlpatterns= [
    re_path(r'^api/orderItems$', views.PostOrderItems, name="postOrderItems"),
]
