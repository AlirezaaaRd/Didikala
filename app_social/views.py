from django.shortcuts import render



def messages(request):
    return render(request , 'profile-comments.html')
# Create your views here.
