import json
from django.shortcuts import render
from .models import orderLines, orders, productMaster
from .serializers import ProductMasterSerializer, OrdersSerializer, OrderLinesSerializer
# from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view


# Create your views here.


@api_view(['GET',])    
def getAllOrderLines(request):
        orderlines = orderLines.objects.all()
        orderline_serializer = OrderLinesSerializer(orderlines, many=True)
        data = orderline_serializer.data
        return JsonResponse(data, safe=False, status=status.HTTP_200_OK)
    
@api_view(['GET',])    
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
        else:
               invalidMessage = body + " is invalid. Please send picked or exeption: meesage"  
               return Response(invalidMessage, status=status.HTTP_201_CREATED)
        return Response(request.body, status=status.HTTP_201_CREATED)

    
@csrf_exempt 
@api_view(['PUT',])
def updateStockCount(request, pk):
        productmaster = get_object_or_404(productMaster, pk=pk)
        pm_serializer = ProductMasterSerializer(productmaster)
        pm_data = pm_serializer.data
        body_unicode = request.body.decode('utf-8')
        qty = json.loads(body_unicode)
        newQty = pm_data['on_hand'] = pm_data['on_hand'] - qty
        if newQty < 1:
                return Response(ProductMasterSerializer(productmaster).data, status=status.HTTP_409_CONFLICT)

        productmaster.on_hand = newQty
        productmaster.save()

        return Response(ProductMasterSerializer(productmaster).data, status=status.HTTP_201_CREATED)

@api_view(['GET',])
def getOneProduct(request, pk):
    product_master = get_object_or_404(productMaster, pk=pk)
    pm_serializer = ProductMasterSerializer(product_master)
    data = pm_serializer.data
    return JsonResponse(data, status=status.HTTP_200_OK) 

@api_view(['GET',])
def getAllProducts(request):
    allProducts = productMaster.objects.all()
    pm_serializer = ProductMasterSerializer(allProducts, many=True)
    data = pm_serializer.data
    return JsonResponse(data, status=status.HTTP_200_OK, safe=False)


@api_view(['GET',])
def getAllOrders(request):
       orders_local = orders.objects.all().order_by('order_date').values() #order by date
       order_serializer = OrdersSerializer(orders_local, many=True)
       data = order_serializer.data
       return JsonResponse(data, safe=False, status=status.HTTP_200_OK)

@api_view(['GET',])
def getOneOrder(request, pk):
       order = get_object_or_404(orders, pk=pk)
       order_serializer = OrdersSerializer(order)
       data = order_serializer.data

       return JsonResponse(data, safe=False, status=status.HTTP_200_OK)


@api_view(['GET',])
def getOrderLineFromOrderNumber(request, on):
       orderline = orderLines.objects.filter(order_number=on)
       orderline_serializer = OrderLinesSerializer(orderline, many=True)
       data = orderline_serializer.data
#        print(data)

       return JsonResponse(data, safe=False, status=status.HTTP_200_OK)
       

 #post api for sending info of failed       