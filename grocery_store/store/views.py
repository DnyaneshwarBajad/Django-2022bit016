from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate

from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.


def register(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.success(request, "Registration successful!")
            return redirect('login')
    return render(request, 'register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials")
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('login')

#from django.shortcuts import render, redirect
from .models import Product

def dashboard(request):
    products = Product.objects.all()
    return render(request, 'dashboard.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        stock = request.POST['stock']
        description = request.POST['description']
        Product.objects.create(name=name, price=price, stock=stock, description=description)
        return redirect('dashboard')
    return render(request, 'add_product.html')



from .models import Cart

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    return render(request, 'cart.html', {'cart_items': cart_items})
