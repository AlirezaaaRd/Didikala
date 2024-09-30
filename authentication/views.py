from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login , logout , authenticate
from django.contrib import messages
from django.contrib.auth.models import User  # Import the built-in User model
from .models import Profile  # Import your Profile model
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.db.models import Q
from .models import Address


def edit_profile(request):
    context = {}
    if request.user.is_authenticated == False:
        return redirect('index')
    elif request.method == 'POST': 

        user = request.user  # Get the current user
        profile = user.profile  # Access the associated Profile

        First_name = request.POST.get('first_name')
        Last_name = request.POST.get('last_name')
        Email = request.POST.get('email')
        national_code = request.POST.get('national_code')
        Phone_number = request.POST.get('phone_number')
        print('1')
        if validate_email(Email) == False:
            context['error'] = "ایمیل معتبر نیست"
            return render(request, 'profile-additional-info.html' , context)

        if not Phone_number.isdigit() or len(Phone_number) != 11:
            context['error'] = "شماره تلفن معتبر نیست"
            return render(request, 'profile-additional-info.html' , context)

        if not national_code.isdigit():  # Check for valid national code
            context['error'] = "کد ملی معتبر نیست"
            return render(request, 'profile-additional-info.html' , context)

        # Check for duplicate email or phone number (excluding the current user)
        if User.objects.filter(Q(email=Email) | Q(profile__phone_number=Phone_number)).exclude(pk=user.pk).exists():
            context['error'] = "ایمیل یا شماره تلفن وارد شده تکراری است."
            return render(request, 'profile-additional-info.html', context)
        else:


            # Update user
            user.first_name = First_name
            user.last_name = Last_name
            user.email = Email
            user.save()

            # Update profile
            profile.national_code = national_code
            profile.phone_number = Phone_number  # Update phone number in Profile model
            profile.save()

            messages.success(request, 'اطلاعات پروفایل شما با موفقیت بروزرسانی شد.')
            return redirect('authentication:profile')  # Redirect to the user's profile page



    else:
        return render(request , 'profile-additional-info.html')

def profile(request):
    return render(request , 'profile.html')

def addresses(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Phone_number = request.POST.get('phone_number')
        city = request.POST.get('city')
        state = request.POST.get('state')
        postal_code = request.POST.get('postal_code')
        description = request.POST.get('description')
        

        # Assuming user is logged in
        user = request.user
        # Create and save a new Address object
        Address.objects.create(
            user=user,
            name=name,
            phone_number=Phone_number,
            city=city,
            state=state,
            postal_code=postal_code,
            description=description
        )

        # Redirect to the same page or another page after saving
        return redirect('authentication:addresses')  # Use the name of your address listing view or another page

    # Fetch all addresses for the logged-in user
    user_addresses = Address.objects.filter(user=request.user)

    return render(request, 'profile-addresses.html', {'addresses': user_addresses})

def edit_address(request):
    if request.method == 'POST':
        address_id = request.POST.get('address_id')
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        state = request.POST.get('state')
        city = request.POST.get('city')
        postal_code = request.POST.get('postal_code')

        # Update the address
        Address.objects.filter(id=address_id).update(
            name=name,
            phone_number=phone_number,
            state=state,
            city=city,
            postal_code=postal_code
        )

    user_addresses = Address.objects.filter(user=request.user)

    return render(request, 'profile-addresses.html', {'addresses': user_addresses})

def register(request):
    if request.user.is_authenticated:
        return redirect('index')  # Redirect to index if already logged in
    context = { 
       "error": "اگر قبلا با ایمیل ثبت‌نام کرده‌اید، نیاز به ثبت‌نام مجدد با شماره همراه ندارید"
   }
    if request.method == 'POST':
        Username = request.POST.get('username')
        Email = request.POST.get('email')
        Password1 = request.POST.get('password1')
        Password2 = request.POST.get('password2')
        Phone_number = request.POST.get('phone_number')




        # Check if username , Email , phoneNumber is already taken
        if User.objects.filter(username=Username).exists():
            context['error'] = 'نام کاربری قبلا گرفته شده است.'
            return render(request, 'register.html' , context)     
        elif User.objects.filter(email=Email).exists():
            context['error'] = 'ایمیل قبلا گرفته شده است.'
            return render(request, 'register.html' , context)
        elif Profile.objects.filter(phone_number=Phone_number).exists():
            context['error'] = 'شماره تلفن قبلا گرفته شده است.'
            return render(request, 'register.html' , context)

        # Check if passwords match
        elif Password1 != Password2:
            context['error'] = 'رمز عبور و تکرار آن باید یکسان باشند.'
            # messages.error(request, 'رمز عبور و تکرار آن باید یکسان باشند.')
            return render(request, 'register.html' , context)
        
        elif not Phone_number.isdigit() and len(Phone_number) != 11:
            context['error'] = "شماره تلفن معتبر نیست"
            return render(request, 'register.html' , context)
        
        elif validate_email(Email) == False:
            context['error'] = "ایمیل معتبر نیست"
            return render(request, 'register.html' , context)
        
        else:
            # Create a new user
            user = User.objects.create_user(username=Username, email=Email, password=Password1)

            # Create a Profile instance associated with the new user
            profile = Profile.objects.create(
                user=user,
                phone_number=Phone_number,
                # ... other profile fields (national_code, card_no) if needed 
            )

            login(request, user)
            # Redirect to the home page
            return redirect('authentication:welcome')

    else:
        return render(request, 'register.html' , context)


def welcome(request):
    return render(request, 'welcome.html')



def my_logout(request):
    logout(request)  # Logs out the user
    return redirect('mainapp:homepage')

def my_login(request):
    if request.user.is_authenticated:
        return redirect('mainapp:homepage')  # Redirect to index if already logged in
    
    elif request.method == 'POST':
        Username = request.POST.get('username')
        Password = request.POST.get('password')
        user = authenticate(username=Username, password=Password)
        if user is not None:
            login(request, user)
            messages.success(request, 'ثبت نام با موفقیت انجام شد! اکنون وارد حساب کاربری خود شده‌اید.')
            return redirect('mainapp:homepage')
        else:
            messages.error(request, 'نام کاربری و یا رمز ورود اشتباه است')
            return redirect('mainapp:homepage')
    else:
        return render(request , 'login.html')


def favorites(request):
    return render(request, 'profile-favorites.html')





def validate_email(email):
    validator = EmailValidator()

    try:
        validator(email)
        return True
    except ValidationError:
        return False