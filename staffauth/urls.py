from django.urls import path
from .views import staff_login, staff_dashboard
from . import views

urlpatterns = [
    path("login/", views.staff_login, name="login"),
    path('dashboard/', staff_dashboard, name='staff_dashboard'),
]