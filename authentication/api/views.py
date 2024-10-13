from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from authentication.api.serializers import Userseralizers

User = get_user_model()




@api_view(['GET'])
def api_all_Users(request):
    User_list = User.objects.all()
    data = Userseralizers(User_list , many = True).data
    return Response(data)



@api_view(['DELETE'])
def api_delete_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    # Delete the user
    user.delete()
    return Response({'message': 'User deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
