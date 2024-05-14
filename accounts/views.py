from django.shortcuts import render
from django.contrib.auth.views import PasswordResetView
# Create your views here.

def home(request):
    return render(request, 'accounts/home.html')

def aboutus(request):
    return render(request, 'accounts/aboutus.html')

def contactus(request):
    return render(request, 'accounts/contactus.html')

def signup(request):
    return render(request, 'accounts/signup.html')

def login(request):
    return render(request, 'accounts/login.html')

class CustomPasswordResetView(PasswordResetView):
    template_name = 'accounts/password_reset.html'