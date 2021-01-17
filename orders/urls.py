from django.urls import path, re_path
from orders import views

urlpatterns= [
    re_path(r'^api/orders$', views.PostOrders, name="postOrders"),
]

