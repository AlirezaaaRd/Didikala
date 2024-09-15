from django.db import models


class BaseProduct(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    count = models.PositiveIntegerField()
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    images = models.ManyToManyField('app_social.Image')
    
    class Meta:
        abstract = True

class DigitalProduct(models.Model):
    category = models.ForeignKey('app_social.Category', on_delete=models.CASCADE , related_name='digital_categories', null=True)
    name_EN = models.CharField(max_length=255 , null=True)

class ClothesProduct(models.Model):
    category = models.ForeignKey('app_social.Category', on_delete=models.CASCADE , related_name='clothes_categories' , null=True)

# class FoodProduct(models.Model):
#     base_product = models.OneToOneField(BaseProduct, on_delete=models.CASCADE)
#     taste = models.CharField(max_length=255)

class Brand(models.Model):
    field = models.CharField(max_length=255 , null=True)

class Color(models.Model):
    field = models.CharField(max_length=255 , null=True)
    product = models.ManyToManyField(DigitalProduct)

class Banner(models.Model):
    title = models.CharField(max_length=255 , null=True)


class Image(models.Model):
    banner = models.ForeignKey(Banner , on_delete=models.CASCADE , null=True)
    url = models.CharField(max_length=150 , null=True)
    image = models.ImageField(upload_to='banners' , null=True)
    



