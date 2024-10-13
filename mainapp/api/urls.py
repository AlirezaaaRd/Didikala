
from django.urls import path , include
from rest_framework.routers import DefaultRouter
from mainapp.api import views


urlpatterns = [
    path('banner/' , views.api_banner , name= 'api-banner'),
    path('product/' , views.api_products , name= 'api-products'),
    path('product/delete/' , views.api_product_delete , name= 'api-products-delete'),
    path('product/create/' , views.api_product_create , name= 'api-products-create'),
    path('product/update/<int:product_id>/' , views.api_product_update , name= 'api-products-update')
]