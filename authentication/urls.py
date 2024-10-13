from django.urls import path , include
from authentication import views

app_name = 'authentication'

urlpatterns = [
    path('' , views.profile , name='profile') ,
    path('edit/' , views.edit_profile , name='edit_profile'),
    path('register/' , views.register , name='register'),
    path('login/' , views.my_login , name='login'),
    path('logout/' , views.my_logout , name='logout'),
    path('welcome/' , views.welcome , name='welcome'),
    path('favorites/' , views.favorites , name='favorites'),
    path('adresses/' , views.addresses , name='addresses'),
    path('edit_address/', views.edit_address, name='edit_address'),
    path('api/' , include('authentication.api.urls'))
]