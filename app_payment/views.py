from django.shortcuts import render, redirect, get_object_or_404
from .models import Basket, BasketItem ,Color , DigitalProduct
from mainapp.models import ClothesProduct
# Create your views here.
def cart_manager(request):
    user = request.user

    if not user.is_authenticated:
        # Redirect or return a response for unauthenticated users
        return redirect('authentication:login')  # Redirect to the login page
    

    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        color_id = request.POST.get('color_id')
        count = int(request.POST.get('count', 1))  # Get count, default to 1 if not provided
        
        # Retrieve the product and color (color can be optional)
        product = DigitalProduct.objects.filter(id=product_id).first()

        if not product:
            product = ClothesProduct.objects.filter(id=product_id).first()

        color = get_object_or_404(Color, id=color_id) if color_id else None
        
        # Get or create the user's basket
        basket, created = Basket.objects.get_or_create(user=user)
        
        # Check if the product already exists in the basket with the same color
        basket_item = BasketItem.objects.filter(basket=basket, product=product, color=color).first()
        
        if basket_item:
            # If the item already exists, update the count
            basket_item.count += count
            basket_item.save()
        else:
            # Otherwise, create a new basket item
            BasketItem.objects.create(
                basket=basket,
                product=product,
                color=color,
                count=count
            )

        userbasket = get_object_or_404(Basket, user=request.user)
        # Get all items in the user's basket
        basket_items = BasketItem.objects.filter(basket=basket)
        context = {
            'basket': userbasket,
            'basket_items': basket_items
        }
        return render(request, 'cart.html' , context)
    
    else:
        basket = Basket.objects.get(user=user)
        if BasketItem.objects.filter(basket=basket).exists():

            userbasket = get_object_or_404(Basket, user=request.user)
            # Get all items in the user's basket
            basket_items = BasketItem.objects.filter(basket=basket)
            context = {
                'basket': userbasket,
                'basket_items': basket_items
        }
            return render(request, 'cart.html' , context)
        else:
            return render(request, 'cart-empty.html')
        

def delete_basket_item(request, item_id):
    if request.method == 'POST' and request.user.is_authenticated:
        basket_item = get_object_or_404(BasketItem, id=item_id, basket__user=request.user)
        basket_item.delete()
        return redirect('app_payment:cart')  # Replace with the name of your basket view
    return redirect('app_payment:cart')  # Handle cases where the method is not POST