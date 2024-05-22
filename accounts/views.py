from django.shortcuts import render, redirect
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'accounts/home.html')

def aboutus(request):
    return render(request, 'accounts/aboutus.html')

def contactus(request):
    return render(request, 'accounts/contactus.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, 'Account created successfully')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
    
    return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('home')  # redirect to the home page or dashboard
        else:
            messages.error(request, 'Invalid credentials')
    
    return render(request, 'accounts/login.html')


class CustomPasswordResetView(PasswordResetView):
    template_name = 'accounts/password_reset.html'