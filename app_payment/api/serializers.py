from rest_framework import serializers
from app_payment.models import Basket , BasketItem
from mainapp.models import Product , Category


class Category_serializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id' , 'name']



class Product_serializer(serializers.ModelSerializer):

    category = serializers.SerializerMethodField()

    def get_category(self, obj):
        return Category_serializer(obj.category.all() , many = True).data

    class Meta:
        model = Product
        fields = [
            'id' ,
            'name' , 'price',
            'count', 'brand',
            'category', 'name_EN',
            'color',  'is_suggested'
        ]



class Basket_Item_serializer(serializers.ModelSerializer):

    product = serializers.SerializerMethodField()

    def get_product(self , obj):
        return Product_serializer(obj.product).data

    class Meta:
        model = BasketItem
        fields = ['id' , 'count' , 'product' , 'color']



class Basket_serializer(serializers.ModelSerializer):

    Basket_Item = serializers.SerializerMethodField()

    def get_Basket_Item(self , obj):
        Basket_Items = obj.basketitem_set.all()
        return Basket_Item_serializer(Basket_Items , many = True).data




    class Meta:
        model = Basket
        fields = '__all__'
