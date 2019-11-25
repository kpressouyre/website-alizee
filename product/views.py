from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Product

def allProducts(request):
    products = Product.objects.all()
    return render(request, 'product/list.html', {'products': products})

def oneProduct(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    return render(request, 'product/detail.html', {'product': product})