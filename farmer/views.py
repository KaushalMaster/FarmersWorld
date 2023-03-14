from django.shortcuts import render
from .models import product_details, farmer_details

# Create your views here.


def index(request):
    return render(request, 'index.html')


def About(request):
    return render(request, 'About.html')


def Products(request):
    products = product_details.objects.all()

    print(products)
    farmer_city = request.POST.get('search')
    farmers = farmer_details.objects.filter(f_city=farmer_city)

    print(farmers)

    return render(request, 'Products.html', {
        'products': products,
        'farmers': farmers
    })


def Contact(request):
    return render(request, 'Contact.html')


# def login(request):
#     return render(request, 'Login.html')


# def register(request):
#     return render(request, 'Register.html')
