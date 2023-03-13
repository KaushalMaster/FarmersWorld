from django.contrib import admin
from .models import farmer_details, customer_details, product_details, nutritionist_details, order_details, payment_details
# Register your models here.
admin.site.register(farmer_details)
admin.site.register(customer_details)
admin.site.register(product_details)
admin.site.register(nutritionist_details)
admin.site.register(order_details)
admin.site.register(payment_details)
