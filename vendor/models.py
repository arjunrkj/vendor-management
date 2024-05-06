from django.db import models
from django.db.models import JSONField

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    def update_historical_performance(self):
        historical_performance, created = HistoricalPerformance.objects.get_or_create(vendor=self)
        historical_performance.average_response_time = self.average_response_time
        historical_performance.save()

    def update_historical_performance_metrics(self):
        historical_performance, created = HistoricalPerformance.objects.get_or_create(vendor=self)
        historical_performance.on_time_delivery_rate = self.on_time_delivery_rate
        historical_performance.quality_rating_avg = self.quality_rating_avg
        historical_performance.fulfillment_rate = self.fulfillment_rate
        historical_performance.save()


class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()    # ISO 8601
    delivery_date = models.DateTimeField()
    items = JSONField(default=dict)
    quantity = models.IntegerField()
    status = models.CharField(max_length=50)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    

class HistoricalPerformance(models.Model):
    vendor = models.OneToOneField(Vendor, on_delete=models.CASCADE, primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)
