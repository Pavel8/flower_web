from django.urls import path
from . import views  # Import views z aktuální aplikace

urlpatterns = [
    path('', views.order_list, name='order_list'),  # Seznam objednávek
    path('<int:order_id>/', views.order_detail, name='order_detail'),  # Detail objednávky
    path('create/', views.create_order, name='create_order'),  # Vytvoření objednávky
]
