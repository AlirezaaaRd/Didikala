from rest_framework.decorators import api_view
from rest_framework import viewsets , status
from rest_framework.response import Response
from mainapp.models import Product , Banner , Category , Brand , Image , Color
from mainapp.api.serializers import ProductSerializer , BannerSerializer
from django.contrib.contenttypes.models import ContentType
from django.views.decorators.csrf import csrf_exempt


@api_view(['GET'])
def api_banner(request):
    banner_list = Banner.objects.all()
    return Response(BannerSerializer(banner_list , many = True).data , 200)




@api_view(['GET'])
def api_products(request):
    Product_list = Product.objects.all()
    return Response(ProductSerializer(Product_list , many = True).data , 200)



@api_view(['DELETE'])
def api_product_delete(request):
    prod_id = request.POST.get('prod_id')
    if prod_id is not None:
        try:
            product = Product.objects.get(id=prod_id)
            product.delete()
            return Response({'message': 'Deleted successfully'} , status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist as err:
            return Response({'message': err} , status.HTTP_400_BAD_REQUEST)
        except ValueError as err:
            return Response({'message': err} , status.HTTP_400_BAD_REQUEST)
        
    return Response({'message': 'prod_id required'} , status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def api_product_create(request):
    name = request.data.get('name')
    price = request.data.get('price')
    count = request.data.get('count')
    brand_id = request.data.get('brand_id')
    category_id = request.data.get('category_id')
    name_EN = request.data.get('name_EN')
    color_ids = request.data.get('color_ids', [])
    is_suggested = request.data.get('is_suggested', False)
    images = request.FILES.getlist('images')

    try:
        category = Category.objects.get(id=category_id)
        brand = Brand.objects.get(id=brand_id)
        colors = Color.objects.filter(id__in=color_ids)
    except (Category.DoesNotExist, Brand.DoesNotExist):
        return Response({'error': 'Invalid category or brand ID'}, status=status.HTTP_400_BAD_REQUEST)

    # Create the product instance
    product = Product.objects.create(
        name=name,
        price=price,
        count=count,
        brand=brand,
        name_EN=name_EN,
        is_suggested=is_suggested
    )
    product.category.add(category)
    product.color.set(colors)

    # Save images and associate them with the product
    content_type = ContentType.objects.get_for_model(Product)
    for image_file in images:
        Image.objects.create(
            content_type=content_type,
            object_id=product.id,
            image=image_file
        )

    return Response({'message': 'Product created successfully'}, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
def api_product_update(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    # Get data from request
    name = request.data.get('name', product.name)
    price = request.data.get('price', product.price)
    count = request.data.get('count', product.count)
    brand_id = request.data.get('brand_id', product.brand.id if product.brand else None)
    category_id = request.data.get('category_id')
    name_EN = request.data.get('name_EN', product.name_EN)
    color_ids = request.data.get('color_ids', [color.id for color in product.color.all()])
    is_suggested = request.data.get('is_suggested', product.is_suggested)
    images = request.FILES.getlist('images', None)  # Optional, only update if new images are provided

    # Update the brand and category if provided
    try:
        brand = Brand.objects.get(id=brand_id) if brand_id else product.brand
    except Brand.DoesNotExist:
        return Response({'error': 'Invalid brand ID'}, status=status.HTTP_400_BAD_REQUEST)

    if category_id:
        try:
            category = Category.objects.get(id=category_id)
            product.category.clear()
            product.category.add(category)
        except Category.DoesNotExist:
            return Response({'error': 'Invalid category ID'}, status=status.HTTP_400_BAD_REQUEST)

    # Update colors
    if color_ids:
        colors = Color.objects.filter(id__in=color_ids)
        product.color.set(colors)

    # Update product fields with new values or retain existing ones if null
    product.name = name
    product.price = price
    product.count = count
    product.brand = brand
    product.name_EN = name_EN
    product.is_suggested = is_suggested
    product.save()

    # If new images are provided, replace the existing ones
    if images:
        # Delete old images (if you want to replace them)
        Image.objects.filter(
            content_type=ContentType.objects.get_for_model(Product),
            object_id=product.id
        ).delete()
        
        # Add new images
        content_type = ContentType.objects.get_for_model(Product)
        for image_file in images:
            Image.objects.create(
                content_type=content_type,
                object_id=product.id,
                image=image_file
            )

    return Response({'message': 'Product updated successfully'}, status=status.HTTP_200_OK)

