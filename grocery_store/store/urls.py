from django.urls import path
from . import views

urlpatterns = [
     path('', views.dashboard, name='dashboard'),  # Directly show dashboard on root URL
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/',views.register,name='register'),
     path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
     
    path('add-product/', views.add_product, name='add_product'),
    
     path('cart/', views.view_cart, name='cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
]
