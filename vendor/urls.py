from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('vendors/',views.listvendors,name='vendors-view'),
    path('vendors/create',views.createvendor,name='vendors-view'),
]
