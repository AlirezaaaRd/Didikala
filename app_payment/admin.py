from django.contrib import admin

from .models import (
    Order, OrderItem, 
    Basket, BasketItem, Transaction
)

class BasketItemInLine(admin.StackedInline):
    model = BasketItem
    extra = 1

admin.site.register(Order)
admin.site.register(OrderItem)

@admin.register(Basket)
class basketadmin(admin.ModelAdmin):
    inlines = [BasketItemInLine]


admin.site.register(BasketItem)
admin.site.register(Transaction)



# Register your models here.
