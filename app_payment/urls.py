from django.urls import path , include
from app_payment import views


app_name = 'app_payment'


urlpatterns = [
path('cart/' , views.cart_manager , name='cart'),
path('cart/<int:item_id>/' , views.delete_basket_item , name='delete_basket_item'),
path('api/' , include('app_payment.api.urls') )
]