from django.urls import path
from . import views  # Import views z aktuální aplikace
from .views import create_order, order_list, order_detail


urlpatterns = [
    path('list/', order_list, name='order_list'),
    path('<int:order_id>/', views.order_detail, name='order_detail'),  # Detail objednávky
    path('create/', views.create_order, name='create_order'),  # Vytvoření objednávky
    path('<int:order_id>/', order_detail, name='order_detail'),
    path('thankyou/', views.thankyou, name='thankyou'),
]
