from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def About(request):
    return render(request, 'About.html')


# def contact(request):
#     return render(request, 'Contact.html')


# def login(request):
#     return render(request, 'Login.html')


# def register(request):
#     return render(request, 'Register.html')
