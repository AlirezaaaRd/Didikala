from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from mainapp.models import Banner , Product , Category , Brand , Color
from django.shortcuts import render, get_object_or_404

def index(request):
    context = {
        'banner_images' : Banner.objects.get(title = 'Main_banners').images ,
        'sidebar_banner_images' : Banner.objects.get(title = 'sidebar_banner').images,
        'product' : Product.objects.all( ),
        'Suggested_product' : Product.objects.filter(is_suggested = True)
    }
    return render(request , 'index.html' , context)

def messages(request):
    return render(request , 'index.html')

def search(request):
    if request.method == 'POST':
        # Get the name of the product or brand
        name = request.POST.get('name', '').strip()

        # Get the selected categories, brands, and colors (they may be multiple)
        selected_categories = request.POST.getlist('category')
        selected_brands = request.POST.getlist('brand')
        selected_colors = request.POST.getlist('color')

        # Get the price range, convert to integers
        min_price = int(request.POST.get('min_price', 0))  # Ensure this is an integer
        max_price = int(request.POST.get('max_price', 10000000))  # Ensure this is an integer

        # Start with all products
        products = Product.objects.all()


        # Filter by name
        if name:
            products = products.filter(name__icontains=name)

        # Filter by categories
        if selected_categories and 'all' not in selected_categories:
            products = products.filter(category__name__in=selected_categories)

        # Filter by brands
        if selected_brands and 'all' not in selected_brands:
            products = products.filter(brand__field__in=selected_brands)

        # Filter by colors
        if selected_colors and 'all' not in selected_colors:
            products = products.filter(color__color__in=selected_colors)

        # Filter by price range
        if min_price and max_price:
            products = products.filter(price__gte=min_price, price__lte=max_price)


        context = {
            'products': products,
            'categories': Category.objects.all(),
            'brands': Brand.objects.all(),
            'colors': Color.objects.all(),
        }

        return render(request, 'search.html', context)

    else:
        context = {
        'products' : Product.objects.all( ),
        'categories' : Category.objects.all(),
        'brands' : Brand.objects.all(),
        'colors' : Color.objects.all(),  
        }
        
    return render(request , 'search.html' , context)

def product_detail(request , id):
        # Try to get the product as a DigitalProduct or ClothesProduct
    context = {}
    try:
        context['product'] = Product.objects.get(id=id)
    except Product.DoesNotExist:
            return render(request, '404.html', status=404)
    
    # Render the template with the product and product_type context
    return render(request, 'single-product.html', context)


 
# Create your views here.
