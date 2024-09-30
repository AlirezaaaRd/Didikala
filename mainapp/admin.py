from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import (
    Brand, ClothesProduct, Color, 
    DigitalProduct , Image , Banner , Category
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

@admin.register(DigitalProduct)
class DigitalProductAdmin(admin.ModelAdmin):
    inlines = [BImageInLine]
    pass

@admin.register(ClothesProduct)
class ClothesProductAdmin(admin.ModelAdmin):
    inlines = [BImageInLine]
    pass