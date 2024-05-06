from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home_page, name='home-page'),
    # Create a new vendor
    path('api/vendors/create/', views.create_vendor, name='vendors-create'),
    
    # List all vendors
    path('api/vendors/', views.list_vendors, name='vendors-list'),
    
    # Retrieve a specific vendor's details
    path('api/vendors/<str:pk>/', views.get_vendor, name='vendor-detail'),
    
    # Update a vendor
    path('api/vendors/<str:pk>/update/', views.update_vendor, name='vendor-update'),
    
    # Delete a specific vendor
    path('api/vendors/<str:pk>/delete/', views.delete_vendor, name='vendor-delete'),

    # Create a purchase History
    path('api/purchase_orders/create/', views.create_purchase, name='purchase-create'),

    #List Purchase orders (to list purchase orders of a specific vendor include /?vendor_id="id" in the url)
    path('api/purchase_orders/', views.list_purchase_orders, name='purchase-list'),

    #list specific purchase order based on po_number
    path('api/purchase_orders/<str:po_number>/', views.get_purchase_order, name='purchase-detail'),

    #update purchase order based on po_number
    path('api/purchase_orders/<str:po_number>/update/', views.update_purchase_order, name='purchase-update'),

    #delete purchase order based on po_number
    path('api/purchase_orders/<str:po_number>/delete/', views.delete_purchase_order, name='purchase-delete'),

    #get performance history by vendor id
    path('api/vendors/<str:pk>/performance/', views.get_performance, name='performance-get'),




]
