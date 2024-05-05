from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from datetime import datetime
from django.shortcuts import get_object_or_404,redirect,render
from .models import Vendor,PurchaseOrder,HistoricalPerformance
from .serializers import VendorSerializer, VendorCreateSerializer, PurchaseOrderSerializer, HistoricalPerformanceSerializer

@api_view(['GET'])
def list_vendors(request):
    vendors = Vendor.objects.all()
    if vendors:
        serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data)
    else:
        return Response({"message": "No vendors exist"}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
def create_vendor(request):
    serializer = VendorCreateSerializer(data=request.data)
    if serializer.is_valid():
        vendor_instance = serializer.save()
        
        # Creating performance instance
        historical_performance = HistoricalPerformance.objects.create(
            vendor=vendor_instance,
            date=datetime.now(),
        )
        historical_performance.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def get_vendor(request, pk):
    vendor_instance = get_object_or_404(Vendor, pk=pk)
    serializer = VendorSerializer(vendor_instance)
    return Response(serializer.data)

@api_view(['PUT'])
def update_vendor(request, pk):
    vendor_instance = get_object_or_404(Vendor, pk=pk)
    serializer = VendorCreateSerializer(instance=vendor_instance, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_vendor(request, pk):
    vendor_instance = get_object_or_404(Vendor, pk=pk)
    vendor_instance.delete()
    return Response({"message": "Vendor successfully deleted"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def create_purchase(request):
    serializer = PurchaseOrderSerializer(data=request.data)
    if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_purchase_orders(request):
    vendor_id = request.GET.get('vendor_id')

    if vendor_id:
        purchase_orders = PurchaseOrder.objects.filter(vendor_id=vendor_id)
    else:
        purchase_orders = PurchaseOrder.objects.all()

    if purchase_orders.exists():
        serializer = PurchaseOrderSerializer(purchase_orders, many=True)
        return Response(serializer.data)
    else:
        return Response({"message": "No purchase orders yet"})
    

@api_view(['GET'])
def get_purchase_order(request, po_id):
    purchase_order = get_object_or_404(PurchaseOrder, po_number=po_id)
    serializer = PurchaseOrderSerializer(purchase_order)
    return Response(serializer.data)


@api_view(['PUT'])
def update_purchase_order(request, po_id):
    purchase_order = get_object_or_404(PurchaseOrder, po_number=po_id)
    serializer = PurchaseOrderSerializer(instance=purchase_order, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def delete_purchase_order(request, po_id):
    purchase_order = get_object_or_404(PurchaseOrder, po_number=po_id)
    purchase_order.delete()
    return Response({"message": "Purchase order successfully deleted"}, status=204)


@api_view(['GET'])
def get_performance(request,pk):
    performance  = get_object_or_404(HistoricalPerformance, vendor_id=pk)
    serializer = HistoricalPerformanceSerializer(performance)
    return Response(serializer.data)