from django.urls import path
from . import views  # Import views z aktuální aplikace

urlpatterns = [
    path('', views.home, name='home'),  # Domovská stránka
    path('about/', views.about, name='about'),  # O stránce
    path('contact/', views.contact, name='contact'),  # Kontakt
]
