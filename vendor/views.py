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
