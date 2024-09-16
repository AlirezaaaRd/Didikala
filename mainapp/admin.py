from django.contrib import admin
from .models import (
    Brand, ClothesProduct, Color, 
    DigitalProduct, ClothesProduct , Image , Banner
)
class ImageInLine(admin.StackedInline):
    model = Image
    extra = 1


admin.site.register(ClothesProduct)
admin.site.register(Color)
admin.site.register(DigitalProduct)
admin.site.register(Image)
# Register your models here


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    inlines = [ImageInLine]