from rest_framework import serializers
from .models import productMaster, orders, orderLines

class ProductMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = productMaster
        fields = '__all__'

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = orders
        fields = '__all__'

class OrderLinesSerializer(serializers.ModelSerializer):
    order_number = OrdersSerializer()
    sku = ProductMasterSerializer()

    class Meta:
        model = orderLines
        fields = '__all__'
