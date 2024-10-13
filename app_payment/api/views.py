from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.response import Response
from app_payment.models import Basket , BasketItem
from mainapp.models import Product
from app_payment.api.serializers import Basket_serializer
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

@api_view(['GET'])
def api_basket(request):
    basket_list = Basket.objects.all()
    return Response(Basket_serializer(basket_list , many = True).data , status.HTTP_200_OK)


@api_view(['DELETE'])
def basket_delete(request):
    pk = request.POST.get('pk')
    if pk is not None:
        try:
            basket = Basket.objects.get(id=pk)
            basket.delete()
            return Response({'message': 'Deleted successfully'} , status.HTTP_204_NO_CONTENT)
        except Basket.DoesNotExist as err:
            return Response({'message': err} , status.HTTP_400_BAD_REQUEST)
        except ValueError as err:
            return Response({'message': err} , status.HTTP_400_BAD_REQUEST)
        
    return Response({'message': 'pk required'} , status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def api_basket_create(request):
    user_id = request.data.get('user_id' , None)
    product_id = request.data.get('product_id' , None)
    count = request.data.get('count' , None)
    user = User.objects.get(id=user_id)
    basket = Basket.objects.create(user = user)
    product = Product.objects.get(id = product_id)
    BasketItem.objects.create(basket=basket , product = product , count = count)

    return Response({'message' : 'created successfully'} , status.HTTP_200_OK) 