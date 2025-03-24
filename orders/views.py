import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Order, OrderItem, OrderStatus
from .forms import OrderForm
from products.models import Product


def create_order(request):
    """Vytvoření nové objednávky."""
    cart = request.session.get('cart', {})  # Získání košíku z session
    products_dict = {}

    if cart:
        # Načteme všechny produkty, které jsou v košíku
        product_ids = cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        products_dict = {product.id: product for product in products}

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.total_price = sum(products_dict[int(pid)].price * qty for pid, qty in cart.items())

            # Výchozí stav objednávky
            default_status, _ = OrderStatus.objects.get_or_create(name="Nová")
            order.status = default_status
            order.save()

            # Uložit produkty do objednávky
            for product_id, quantity in cart.items():
                product = products_dict[int(product_id)]
                OrderItem.objects.create(order=order, product=product, quantity=quantity, price=product.price)

            # Vymazat košík po objednání
            request.session['cart'] = {}

            return redirect('order_detail', order_id=order.id)
    else:
        form = OrderForm()

    return render(request, 'checkout.html', {'form': form, 'cart': cart, 'products_dict': products_dict})


def order_list(request):
    orders = Order.objects.all().order_by('-created_at')  # Seřazení od nejnovějších
    return render(request, 'order_list.html', {'orders': orders})


def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order_detail.html', {'order': order})
