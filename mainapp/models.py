from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=255 , null = True)
    price = models.PositiveIntegerField(null = True)
    count = models.PositiveIntegerField(null = True)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE , null =True )
    category = models.ManyToManyField('Category')
    name_EN = models.CharField(max_length=255 , null=True)
    color = models.ManyToManyField('Color')
    is_suggested = models.BooleanField(default=False)
    


    @property
    def images(self):
        return Image.objects.filter(
            object_id = self.id , 
            content_type = ContentType.objects.get_for_model(self.__class__).id)
    

    def get_absolute_url(self):
        return reverse('mainapp:product_detail', args = (self.id, ))
    

    def __str__(self):
        return self.name


class Brand(models.Model):
    field = models.CharField(max_length=255 , null=True)
    def __str__(self):
        return self.field

class Color(models.Model):
    color = models.CharField(max_length=255 , null=True)
    hex_value = models.CharField(max_length=255 , null=True)
    def __str__(self):
        return self.color

class Banner(models.Model):
    title = models.CharField(max_length=255 , null=True)

    @property
    def images(self):
        return Image.objects.filter(
            object_id = self.id , 
            content_type = ContentType.objects.get_for_model(self.__class__).id)

    def __str__(self):
        return self.title


class Image(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE , null = True ,related_name='app_store_images')
    object_id = models.PositiveIntegerField(null = True)
    content_object = GenericForeignKey("content_type", "object_id")
    url = models.CharField(max_length=150 , null=True)
    image = models.ImageField(upload_to='banners' , null=True)
    def __str__(self):
        return self.image.url    


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    



