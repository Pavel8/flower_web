from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_cookie, name='create_cookie'),
    path('get/', views.get_cookie, name='get_cookie'),
    path('delete/', views.delete_cookie, name='delete_cookie'),
    path('swap/', views.swap_cookie, name='swap_cookie'),
    path('set-preference/', views.set_cookie_preference, name='set_cookie_preference'),
    path('get-preference/', views.get_cookie_preference, name='get_cookie_preference'),
]
