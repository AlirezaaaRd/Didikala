from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import (
    Brand, Product, Color, 
    Image , Banner , Category
)
# class ImageInLine(admin.StackedInline):
#     model = Image
#     extra = 1

class BImageInLine(GenericStackedInline):
    model = Image
    extra = 1


admin.site.register(Color)
admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Brand)
# Register your models here


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    inlines = [BImageInLine]
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [BImageInLine]
    pass
