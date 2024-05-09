from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'accounts/home.html')

def aboutus(request):
    return render(request, 'accounts/aboutus.html')

def contactus(request):
    return render(request, 'accounts/contactus.html')