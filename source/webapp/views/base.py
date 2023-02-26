from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from webapp.models import Product


def index_view(request: WSGIRequest):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'index.html', context=context)
