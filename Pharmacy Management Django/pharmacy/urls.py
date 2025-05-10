from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),           # Home page
    path('customers/', views.customers, name='customers'),  # Customers page
    path('suppliers/', views.suppliers, name='suppliers'),  # Suppliers page
]

