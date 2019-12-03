from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import About, Contact

from product.models import Product, Image

def index(request):
    about = About.objects.get(pk=1)
    contact = Contact.objects.get(pk=1)
    products = Product.objects.all()
    for product in products:
        product.images = Image.objects.filter(product__pk=product.id)
    return render(request, 'index.html', {'about': about, 'contact': contact, 'products': products})

def about(request):
    try:
        about = About.objects.get(pk=1)
    except Product.DoesNotExist:
        raise Http404("about does not exist")
    return render(request, 'about.html', {'about': about})

def contact(request):
    contact = Contact.objects.get(pk=1)
    return render(request, 'contact.html', {'contact': contact})
