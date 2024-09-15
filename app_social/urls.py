from django.urls import path
from app_social import views


app_name = 'app_social'


urlpatterns = [
path('' , views.messages , name='messages'),
]