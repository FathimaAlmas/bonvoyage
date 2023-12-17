from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile, AdminProfile, HotelProfile


# ADMIN Register
def admin_registration(request):
    if request.method == 'POST':
        username = request.POST[ 'username']
        password1 = request.POST[ 'password1']
        password2 = request.POST[ 'password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email ID Taken')
                return redirect('admin_register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('admin_register')
            else:
                user = User.objects.create_user (password=password1, email=email,username=username)
                AdminProfile.objects.create(user=user,username=username,email=email)
                user.save();
                print('User created')
                return redirect('admin_login')
        else:
            messages.info(request,'Password do not match')
            return redirect('admin_register')
        return redirect('/admin_register')
    else:   
        return render(request, 'base/admin_register.html')


# admin_login
def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_profile', user_id=user.id)
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'base/admin_login.html')

@login_required
def admin_profile(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'base/adminhome.html', {'user': user})


# admin_logout
def admin_logout(request):
    logout(request)
    return redirect('/')


#user register
def user_registration(request):
    if request.method == 'POST':
        username = request.POST[ 'username']
        password1 = request.POST[ 'password1']
        password2 = request.POST[ 'password2']
        email = request.POST['email']
        first_name = request.POST[ 'first_name']
        last_name = request.POST[ 'last_name']
        

        if password1==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email ID Taken')
                return redirect('user_register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('user_register')
            else:
                user = User.objects.create_user (password=password1, email=email,username=username,first_name=first_name,last_name=last_name)
                UserProfile.objects.create(user=user,username=username,email=email)
                user.save();
                print('User created')
                return redirect('user_login')
        else:
            messages.info(request,'Password do not match')
            return redirect('user_register')
        return redirect('/user_register')
    else:   
        return render(request, 'base/user_register.html')
    

# user_login
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_profile', user_id=user.id)
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'base/user_login.html')

@login_required
def user_profile(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'base/index.html', {'user': user})


# user_logout
def user_logout(request):
    logout(request)
    return redirect('/')


#HOTEL REGISTER
def hotel_registration(request):
    if request.method == 'POST':
        username = request.POST[ 'username']
        password1 = request.POST[ 'password1']
        password2 = request.POST[ 'password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email ID Taken')
                return redirect('hotel_register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('hotel_register')
            else:
                user = User.objects.create_user (password=password1, email=email,username=username)
                HotelProfile.objects.create(user=user,username=username,email=email)
                user.save();
                print('User created')
                return redirect('hotel_login')
        else:
            messages.info(request,'Password do not match')
            return redirect('hotel_register')
        return redirect('/hotel_register')
    else:   
        return render(request, 'base/hotel_register.html')
    

# HOTEL LOGIN
def hotel_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('hotel_profile', user_id=user.id)
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'base/hotel_login.html')

@login_required
def hotel_profile(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'base/hotel_home.html', {'user': user})

# HOTEL LOGOUT
def hotel_logout(request):
    logout(request)
    return redirect('/')





# Create your views here.

