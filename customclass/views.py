from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from customclass.models import XYZ_sales_data
from customclass.serializers import XYZ_sales_dataSerializer


@csrf_exempt
def customclass_list(request):
    
    if request.method == 'GET':
        sales_data = XYZ_sales_data.objects.all()
        serializer = XYZ_sales_dataSerializer(sales_data, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = XYZ_sales_dataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
    

@csrf_exempt
def customclass_detail(request, pk):
    
    try:
        x = XYZ_sales_data.objects.get(pk=pk)
    except XYZ_sales_data.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        y = XYZ_sales_dataSerializerr(x)
        return JsonResponse(y.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = XYZ_sales_dataSerializer(x, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        x.delete()
        return HttpResponse(status=204)    
