from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_detail, name='cart'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('add_quantity/<int:product_id>/', views.cart_add_quantity, name='cart_add_quantity'),  # Přidání 1 kusu
    path('remove_quantity/<int:product_id>/', views.cart_remove_quantity, name='cart_remove_quantity'),  # Odebrání 1 kusu
    path('debug/', views.debug_cart, name='debug_cart'),
    path('checkout/', views.checkout, name='checkout'),

]
