from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Vendor,PurchaseOrder,HistoricalPerformance
from .serializers import Vendorserializer,VendorCreateSerializer

# Create your views here.
@api_view(['GET'])
def listvendors(request):
    vendors = Vendor.objects.all()
    if vendors:
        serializer = Vendorserializer(vendors, many=True)
        return Response(serializer.data)
    else:
        return Response({"message": "No vendors found"}, status=404)

@api_view(['POST'])
def createvendor(request):
    serializer = VendorCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return redirect('api/vendors/')
    else:
        return Response(serializer.errors, status=400)  


@api_view(['PUT'])
def updatevendor(request, pk):
    try:
        vendor_toupdate = Vendor.objects.get(id=pk)
    except Vendor.DoesNotExist:
        return Response({"message": "Vendor not found"}, status=404)

    serializer = VendorCreateSerializer(instance=vendor_toupdate, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200) 
    else:
        return Response(serializer.errors, status=400)  
    

@api_view(['GET'])
def getvendor(request,pk):
    try:
        vendor_toget = Vendor.objects.get(id=pk)
    except Vendor.DoesNotExist:
        return Response({"message": "Vendor not found"}, status=404)
    serializer = Vendorserializer(vendor_toget, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
def deletevendor(request, pk):
    try:
        vendor_todelete = Vendor.objects.get(id=pk)
    except Vendor.DoesNotExist:
        return Response({"message": "Vendor not found"}, status=404)
    
    vendor_todelete.delete()
    return Response({"message": "Vendor successfully deleted"}, status=204)
