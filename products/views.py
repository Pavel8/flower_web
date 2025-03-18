from django.shortcuts import render
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from .models import Product

from django.urls import reverse_lazy
from .forms import ProductForm


class ProductListView(ListView):
	model = Product
	products = Product.objects.all()
	template_name = 'product_list.html'
	context_object_name = 'products'


class ProductDetailView(DetailView):
	model = Product

	template_name = 'product_detail.html'
	context_object_name = 'product'


class ProductCreateView(CreateView):
		model = Product
		form_class = ProductForm
		template_name = 'product_form.html'
		success_url = reverse_lazy('product_list')


class ProductUpdateView(UpdateView):
	model = Product

	fields = ['title', 'type', 'alive', 'occasion']
	template_name = 'product_form.html'
	success_url = reverse_lazy('product_list')


class ProductDeleteView(DeleteView):
	model = Product

	template_name = 'product_confirm_delete.html'
	success_url = reverse_lazy('product_list')