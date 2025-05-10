

# Register your models here.
from django.contrib import admin
from .models import Product, Cart  # Import your models

# Register models so they appear in Django Admin
admin.site.register(Product)
admin.site.register(Cart)
