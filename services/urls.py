from django.urls import path
from . import views
from .views import service_detail, staff_service_list

urlpatterns = [
    path('', views.service_list, name='service_list'),  # Seznam služeb
    path('<int:pk>/', service_detail, name='service_detail'),
    path('create/', views.service_create, name='service_create'),  # Vytvoření nové služby
    path('<int:pk>/update/', views.service_update, name='service_update'),  # Úprava služby
    path('<int:pk>/delete/', views.service_delete, name='service_delete'),
    path('staff/services/', staff_service_list, name='staff_service_list'),
]