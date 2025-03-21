from django.shortcuts import render
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from .models import Product, Occasion, Type
from .forms import ProductForm

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = Product.objects.all()
        occasion_id = self.request.GET.get('occasion')
        type_id = self.request.GET.get('type')

        if occasion_id:
            queryset = queryset.filter(occasion__id=occasion_id)
        if type_id:
            queryset = queryset.filter(type__id=type_id)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['occasions'] = Occasion.objects.all()
        context['types'] = Type.objects.all()
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm  # Ujisti se, že formulář zohledňuje nová pole, pokud je to žádoucí. # Změna: Využití vlastního formuláře
    template_name = 'product_form.html'
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        # Zde můžete provést případné úpravy, např. automatické vygenerování slug, pokud nebyl zadán.
        if not form.instance.slug:
            form.instance.slug = form.instance.title.replace(" ", "-").lower()
        return super().form_valid(form)

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm  # Změna: Použití stejného formuláře jako při vytváření, aby byla konzistence polí
    template_name = 'product_form.html'
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        # Pokud potřebujete upravit slug i při aktualizaci
        if not form.instance.slug:
            form.instance.slug = form.instance.title.replace(" ", "-").lower()
        return super().form_valid(form)

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('product_list')
