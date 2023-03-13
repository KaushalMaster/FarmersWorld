from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('About', views.About, name='About'),
    path('Products', views.Products, name='Products'),
    path('Contact', views.Contact, name='Contact'),
    # path('login', views.login, name='login'),
    # path('register', views.register, name='register'),
]
