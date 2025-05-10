from django.contrib import admin
from .models import Medicine, Supplier, Customer, Sale, Inventory

admin.site.register(Medicine)
admin.site.register(Supplier)
admin.site.register(Customer)
admin.site.register(Sale)
admin.site.register(Inventory)

