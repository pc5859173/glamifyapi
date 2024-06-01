from django.shortcuts import render, redirect
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm



from django.shortcuts import get_object_or_404, redirect, render
from .models import Category, Subcategory
from .forms import CategoryForm, SubcategoryForm


from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest
from .models import Product
from .forms import ProductForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
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

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category/category_list.html', {'categories': categories})

def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'category/category_details.html', {'category': category, 'products': products})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('category-list')
    else:
        form = CategoryForm()
    return render(request, 'category/category_create.html', {'form': form})

def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category-list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category/category_update.html', {'form': form, 'category': category})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category-list')
    else:
        return render(request, 'category/category_delete.html', {'category': category})

def subcategory_list(request, category_id):
    category = Category.objects.get(pk=category_id)
    subcategories = category.subcategories.all()
    return render(request, 'category/subcategory_list.html', {'category': category, 'subcategories': subcategories})

def subcategory_create(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST':
        form = SubcategoryForm(request.POST, request.FILES)
        if form.is_valid():
            subcategory = form.save(commit=False)
            subcategory.category = category
            subcategory.save()
            return redirect('subcategory-details', category_id=category_id, pk=subcategory.pk)
    else:
        form = SubcategoryForm()
    return render(request, 'category/subcategory_create.html', {'form': form, 'category': category})

def subcategory_detail(request, category_id, pk):
    category = get_object_or_404(Category, pk=category_id)
    subcategory = get_object_or_404(Subcategory, pk=pk)
    return render(request, 'category/subcategory_details.html', {'category': category, 'subcategory': subcategory})

def subcategory_update(request, pk):
    subcategory = get_object_or_404(Subcategory, pk=pk)
    if request.method == 'POST':
        form = SubcategoryForm(request.POST, request.FILES, instance=subcategory)
        if form.is_valid():
            form.save()
            return redirect('subcategory-details', category_id=subcategory.category.pk, pk=subcategory.pk)
    else:
        form = SubcategoryForm(instance=subcategory)
    return render(request, 'category/subcategory_update.html', {'form': form, 'subcategory': subcategory})

def subcategory_delete(request, pk):
    subcategory = get_object_or_404(Subcategory, pk=pk)
    category_id = subcategory.category.pk
    if request.method == 'POST':
        subcategory.delete()
        return redirect('subcategory-list', category_id=category_id)
    return render(request, 'category/subcategory_delete.html', {'subcategory': subcategory})


def product_list(request):
    query = request.GET.get('query')
    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    else:
        products = Product.objects.all()
    
    paginator = Paginator(products, 3)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    
    return render(request, 'product/product_list.html', {'products': products})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product-list')
    else:
        form = ProductForm()
    return render(request, 'product/product_create.html', {'form': form})

def product_details(request,pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product/product_details.html', {'product': product})


def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product-list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product/product_update.html', {'form': form})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product-list')
        
    return render(request, 'product/product_delete.html', {'deleted_product': product})

