from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from mainapp.models import Banner , ClothesProduct , DigitalProduct
from django.shortcuts import render, get_object_or_404

def index(request):
    context = {
        'banner_images' : Banner.objects.get(title = 'Main_banners').images ,
        'sidebar_banner_images' : Banner.objects.get(title = 'sidebar_banner').images,
        'clothes_product' : ClothesProduct.objects.all( )
    }
    return render(request , 'index.html' , context)

def messages(request):
    return render(request , 'index.html')


def product_detail(request , id):
        # Try to get the product as a DigitalProduct or ClothesProduct
    context = {}
    try:
        context['product'] = DigitalProduct.objects.get(id=id)
        context['product_type'] = 'digital'
    except DigitalProduct.DoesNotExist:
        try:
            context['product'] = ClothesProduct.objects.get(id=id)
            context['product_type'] = 'clothes'
        except ClothesProduct.DoesNotExist:
            # Handle the case where the product doesn't exist
            return render(request, '404.html', status=404)
    
    # Render the template with the product and product_type context
    return render(request, 'single-product.html', context)


 
# Create your views here.
