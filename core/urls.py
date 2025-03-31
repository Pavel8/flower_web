from django.urls import path
from . import views  # Import views z aktuální aplikace
from .views import business_terms_conditions

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('business-terms/', business_terms_conditions, name='business_terms_conditions'),
]
