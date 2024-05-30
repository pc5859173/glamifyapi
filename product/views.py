from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest
from .models import Product
from .forms import ProductForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

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

