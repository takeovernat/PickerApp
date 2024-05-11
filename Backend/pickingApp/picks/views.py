import json
from django.shortcuts import render
from .models import orderLines, orders, productMaster
from .serializers import ProductMasterSerializer, OrdersSerializer, OrderLinesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view


# Create your views here.


    
def getAllOrderLines(request):
        orderlines = orderLines.objects.all()
        orderline_serializer = OrderLinesSerializer(orderlines, many=True)
        data = orderline_serializer.data
        return JsonResponse(data, safe=False, status=status.HTTP_200_OK)
    
def getOneOrderLine(request, pk):
        order_detail = get_object_or_404(orderLines, pk=pk)
        orderline_serializer = OrderLinesSerializer(order_detail)
        data = orderline_serializer.data
        return JsonResponse( data, safe=False, status=status.HTTP_200_OK)

@csrf_exempt 
@api_view(['PUT',])
def updateOLStatus(request, pk):
        order_detail = get_object_or_404(orderLines, pk=pk)
        if request.body:
            body = request.body.decode('utf-8')
        if "picked" in body:
                order_detail.pick_status = "picked"
                order_detail.save()
                orderline_serializer = OrderLinesSerializer(order_detail)
                data = orderline_serializer.data
                return Response(data, status=status.HTTP_201_CREATED)
        elif "exception" in body:
                order_detail.pick_status = body
                print(body)
                order_detail.save()
                orderline_serializer = OrderLinesSerializer(order_detail)
                data = orderline_serializer.data
                return Response(data, status=status.HTTP_201_CREATED)
        return Response(request.body, status=status.HTTP_201_CREATED)

    
@csrf_exempt 
@api_view(['PUT',])
def updateStockCount(request, pk):
        productmaster = get_object_or_404(productMaster, pk=pk)
        body_unicode = request.body.decode('utf-8')
        qty = json.loads(body_unicode)
        # productMaster.onhand = productMaster.onhand - qty
        print(qty)
        return Response(qty)

@api_view(['GET',])
def getAllOrders(request):
       orders_local = orders.objects.all().order_by('order_date').values() #order by date
       order_serializer = OrdersSerializer(orders_local, many=True)
       data = order_serializer.data
       return JsonResponse(data, safe=False, status=status.HTTP_200_OK)

