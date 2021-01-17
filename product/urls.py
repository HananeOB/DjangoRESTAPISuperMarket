from django.urls import path, re_path
from product import views

urlpatterns= [
    re_path(r'^api/products$', views.getProducts, name="getProducts"),
    re_path(r'^api/products/(?P<pk>[0-9]+)$', views.getProductDetail, name="productDetails"),
    re_path(r'^api/products/(?P<name>[A-Za-z]+)$', views.getProductByname, name="productByName"),
]


# path(r'^/products/(?P<pk>[0-9]+)$', views.getProductDetail, name="productDetails"),