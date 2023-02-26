from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Product
from django.http import HttpResponseNotFound
from django.urls import reverse
from static.classes.static import Static


def add_view(request: WSGIRequest):
    if request.method == "GET":
        return render(request, 'product_create.html', context={'choices': Static.choices})

    product_data = {
        'name': request.POST.get('name'),
        'description': request.POST.get('description'),
        'image': request.POST.get('image'),
        'category': request.POST.get('category'),
        'product_left': request.POST.get('product_left'),
        'price': request.POST.get('price')
    }
    product = Product.objects.create(**product_data)
    return redirect('product_detail', pk=product.pk)


def detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', context={
        'product': product
    })


def update_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.name = request.POST.get('name')
        product.description = request.POST.get('description')
        product.image = request.POST.get('image')
        product.category = request.POST.get('category')
        product.product_left = request.POST.get('product_left')
        product.price = request.POST.get('price')
        product.save()
        return redirect('product_detail', pk=product.pk)
    return render(request, 'product_update.html', context={'product': product, 'choices': Static.choices})


def delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_confirm_delete.html', context={'product': product})


def confirm_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('index')
