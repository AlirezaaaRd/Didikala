from django.urls import path
from rest_framework.routers import DefaultRouter
from authentication.api import views


urlpatterns = [
    path('Users/' , views.api_all_Users , name= 'api-banner'),
    path('Users/Delete/<int:user_id>/' , views.api_delete_user , name= 'api-banner'),
]