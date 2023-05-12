from django.db import models
import datetime
import os

# Create your models here.
class XYZ_sales_data(models.Model):
    order_id=models.CharField(max_length=100)
    order_date=models.CharField(max_length=50)
    ship_date=models.CharField(max_length=50)
    ship_mode=models.CharField(max_length=50)
    customer_id=models.CharField(max_length=50)
    customer_name=models.CharField(max_length=100)
    segment=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    postal_code=models.IntegerField(max_length=50)
    region=models.CharField(max_length=50)
    product_id=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    sub_category=models.CharField(max_length=100)
    product_name=models.CharField(max_length=100)
    sales=models.IntegerField(max_length=200)
    
    def __str__(self):
         return self.order_id 