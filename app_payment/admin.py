from django.contrib import admin

from .models import (
    Order, OrderItem, 
    Basket, BasketItem, Transaction
)

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Basket)
admin.site.register(BasketItem)
admin.site.register(Transaction)



# Register your models here.
