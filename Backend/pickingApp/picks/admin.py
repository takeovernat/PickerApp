from django.contrib import admin
from .models import orderLines, orders, productMaster




admin.site.register(orderLines)
admin.site.register(orders)
admin.site.register(productMaster)