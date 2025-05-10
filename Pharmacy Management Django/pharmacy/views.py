from django.shortcuts import render
from .models import Medicine, Supplier, Customer, Sale, Inventory

# Home view to display medicines
def home(request):
    medicines = Medicine.objects.all()
    return render(request, 'pharmacy/home.html', {'medicines': medicines})

# View to display customers
def customers(request):
    customers = Customer.objects.all()
    return render(request, 'pharmacy/customers.html', {'customers': customers})

# View to display suppliers
def suppliers(request):
    suppliers = Supplier.objects.all()
    return render(request, 'pharmacy/suppliers.html', {'suppliers': suppliers})

