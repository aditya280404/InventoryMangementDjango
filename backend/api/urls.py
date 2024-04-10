from django.urls import path
from . import views

urlpatterns = [
    # Product URLs
    path('products/', views.product_list, name='product-list'),
    path('products/<int:pk>/', views.product_detail, name='product-detail'),

    # Order URLs
    path('orders/', views.order_list, name='order-list'),
    path('orders/<int:pk>/', views.order_detail, name='order-detail'),

    # Customer URLs
    path('customers/', views.customer_list, name='customer-list'),
    path('customers/<int:pk>/', views.customer_detail, name='customer-detail'),
]
