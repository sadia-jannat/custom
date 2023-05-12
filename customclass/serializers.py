from rest_framework import serializers
from customclass.models import XYZ_sales_data,datetime

class XYZ_sales_dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = XYZ_sales_data
        fields = ['order_id', 'order_date', 'ship_date', 'ship_mode', 'customer_id', 'customer_name',
                  'segment','country','city','state','postal_code','region','product_id','category','sub_category',
                  'product_name','sales']