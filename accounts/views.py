from django.shortcuts import render, redirect
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
# Create your views here.

def home(request):
    return render(request, 'accounts/home.html')

def aboutus(request):
    return render(request, 'accounts/aboutus.html')

def contactus(request):
    return render(request, 'accounts/contactus.html')

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

@login_required
def cart(request):
    return render(request, 'accounts/cart.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        # Check if all required fields are provided
        if not all([username, email, password, confirm_password]):
            messages.error(request, 'Please fill in all fields')
        else:
            if password == confirm_password:
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'Username already exists')
                elif User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists')
                else:
                    try:
                        user = User.objects.create_user(username=username, email=email, password=password)
                        user.save()
                        messages.success(request, 'Account created successfully')
                        return redirect('login')
                    except Exception as e:
                        messages.error(request, f'Error creating user: {e}')
            else:
                messages.error(request, 'Passwords do not match')
    
    return render(request, 'accounts/signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('home')  # redirect to the home page or dashboard
        else:
            messages.error(request, 'Invalid credentials')
    
    return render(request, 'accounts/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to the home page after logout


class CustomPasswordResetView(PasswordResetView):
    template_name = 'accounts/password_reset.html'