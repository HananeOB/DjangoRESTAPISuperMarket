from django.urls import path, re_path
from . import views

urlpatterns= [
    re_path(r'^api/users$', views.getUsers, name="getUsers"),
    re_path(r'^api/users/(?P<pk>[0-9]+)$', views.getUserDetail, name="userDetails"),
    re_path(r'^api/users/(?P<username>[A-Za-z]+)$', views.getUserByname, name="userByName"),
]
