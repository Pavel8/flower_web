from django.urls import path
from .views import (ProductListView, ProductDetailView, staff_product_list,
                    ProductCreateView, ProductUpdateView, ProductDeleteView)


urlpatterns = [
    path('list/', ProductListView.as_view(), name="product_list"),
    path('detail/<int:pk>', ProductDetailView.as_view(), name="product_detail"),
    path('add/', ProductCreateView.as_view(), name="product_create"),
    path('update/<int:pk>', ProductUpdateView.as_view(), name="product_update"),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name="product_delete"),
    path('staff/products/', staff_product_list, name='staff_product_list'),
]