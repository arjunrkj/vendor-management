from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('vendors/',views.listvendors,name='vendors-view'),
    path('vendors/create/',views.createvendor,name='vendors-create'),
    path('vendors/update/<str:pk>/',views.updatevendor,name='vendors-update'),
    path('vendors/getvendor/<str:pk>/',views.getvendor,name='vendor-get'),
    path('vendors/deletevendor/<str:pk>/',views.deletevendor,name='vendor-delete'),
]
