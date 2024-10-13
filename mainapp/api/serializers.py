from mainapp.models import Product , Banner , Image
from rest_framework import serializers
from django.conf import settings

class ProductSerializer(serializers.ModelSerializer):

    image_list = serializers.SerializerMethodField()

    def get_image_list(self , obj):
        return Imageserializers(obj.images , many = True).data
    
    class Meta:
        model = Product
        fields = ['id' ,'name' , 'price','image_list',
            'count', 'brand','category',
            'name_EN','color', 'is_suggested']

class Imageserializers(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self , obj):
        return settings.DOMAIN + obj.image.url

    class Meta:
        model = Image
        fields = ['id' , 'image' , 'url']


class BannerSerializer(serializers.ModelSerializer):
    image_list = serializers.SerializerMethodField()

    def get_image_list(self , obj):
        return Imageserializers(obj.images , many = True).data
        # return [
        #     {
        #         'imag' : settings.DOMAIN + img.image.url,
        #         'url' : img.url
        #     }
        #      for img in obj.images]

    class Meta:
        model = Banner
        fields = ['id' , 'title' , 'image_list']