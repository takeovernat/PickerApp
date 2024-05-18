"""
URL configuration for pickingApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from picks.views import *
from picks import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #order lines
    path("orderlines/", views.getAllOrderLines, name="orders-lines" ),
    path('orderlines/<int:pk>', views.getOneOrderLine, name='order-detail'),
    path('orderlines/update/<int:pk>', views.updateOLStatus, name='order-update'),
    path("orderlines/pending", views.getLinebyStatus , name="lines_by_status"),
    path("orderlines/regected", views.getRegectedLines, name="regected"),

    #product master
    path ('productmaster/', views.getAllProducts, name="get-products"),
    path('productmaster/<int:pk>', views.getOneProduct, name="get-product"),
    path('productmaster/update/<int:pk>', views.updateStockCount, name='product-update'),
    path('productmaster/outofstock', views.productOutOfStock, name="outofstock"),

    #orders
    path('orders/', views.getAllOrders, name="all-orders"), #idealy we would limit this to a date
    path('orders/<str:pk>', views.getOneOrder, name="one-order"),
    path('linefromorder/<str:on>', views.getOrderLineFromOrderNumber, name="line-from-order")
]
