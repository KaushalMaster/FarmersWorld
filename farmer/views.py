from django.shortcuts import render
from .models import product_details

# Create your views here.


def index(request):
    return render(request, 'index.html')


def About(request):
    return render(request, 'About.html')


def Products(request):
    products = product_details.objects.all()
    print(products)
    return render(request, 'Products.html', {
        'products': products
    })


def Contact(request):
    return render(request, 'Contact.html')


# def login(request):
#     return render(request, 'Login.html')


# def register(request):
#     return render(request, 'Register.html')
