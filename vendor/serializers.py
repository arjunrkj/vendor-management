from rest_framework import serializers
from .models import Vendor,PurchaseOrder,HistoricalPerformance

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'


class VendorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['name', 'contact_details', 'address', 'vendor_code']
        

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'

    def create(self, validated_data):
        purchase_order = PurchaseOrder.objects.create(**validated_data)

        # Calculate the average response time for the vendor
        vendor = purchase_order.vendor
        vendor_purchase_orders = PurchaseOrder.objects.filter(vendor=vendor)
        response_times = [
            (po.acknowledgment_date - po.issue_date).total_seconds()
            for po in vendor_purchase_orders
            if po.acknowledgment_date is not None
        ]
        if response_times:
            average_response_time = sum(response_times) / len(response_times)
            vendor.average_response_time = average_response_time
            vendor.save()

            # Update the vendor's historical performance
            vendor.update_historical_performance()

        return purchase_order

class HistoricalPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPerformance
        fields = '__all__'