
from django.urls import path , include
from app_payment.api import views



urlpatterns = [
    path('basket/' , views.api_basket , name= 'api-basket'),
    path('basket/delete/' , views.basket_delete , name= 'api-basket-delete'),
    path('basket/create/' , views.api_basket_create , name= 'api-basket-create'),

   
]