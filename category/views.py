from django.shortcuts import get_object_or_404, redirect, render
from .models import Category, Subcategory
from product.models import Product, Category
from .forms import CategoryForm, SubcategoryForm

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
