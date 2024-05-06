from rest_framework import serializers
from .models import Vendor,PurchaseOrder,HistoricalPerformance
from django.db.models import Avg, Count
from datetime import datetime

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

    def update(self, instance, validated_data):
        purchase_order = super().update(instance, validated_data)
        self.update_vendor_performance_metrics()
        return purchase_order

    def update_vendor_performance_metrics(self):
        vendor = self.instance.vendor
        vendor_purchase_orders = PurchaseOrder.objects.filter(vendor=vendor)

        # Calculate On-Time Delivery Rate
        completed_on_time_orders = vendor_purchase_orders.filter(
            status='completed', delivery_date__lte=self.instance.delivery_date
        ).count()
        completed_orders = vendor_purchase_orders.filter(status='completed').count()
        vendor.on_time_delivery_rate = completed_on_time_orders / completed_orders if completed_orders else 0.0

        # Calculate Quality Rating Average
        completed_orders_with_quality_rating = vendor_purchase_orders.exclude(quality_rating__isnull=True).filter(status='completed')
        vendor.quality_rating_avg = completed_orders_with_quality_rating.aggregate(Avg('quality_rating'))['quality_rating__avg'] or 0.0

        # Calculate Fulfillment Rate
        successfully_fulfilled_orders = vendor_purchase_orders.filter(status='completed').count()
        total_orders = vendor_purchase_orders.count()
        vendor.fulfillment_rate = successfully_fulfilled_orders / total_orders if total_orders else 0.0

        #updating vendor's instance
        vendor.save()

        #updating vendor's historical performance instance
        vendor.update_historical_performance_metrics()

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