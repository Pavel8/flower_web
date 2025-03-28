import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Order, OrderItem, OrderStatus
from .forms import OrderForm
from products.models import Product
import logging

logger = logging.getLogger(__name__)  # Přidání logování


def create_order(request):
    """Vytvoření nové objednávky."""
    cart = request.session.get('cart', {})
    products_dict = {}

    logger.debug(f"Obsah košíku při začátku objednávky: {cart}")

    if cart:
        product_ids = cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        products_dict = {str(product.id): product for product in products}

    if request.method == 'POST':
        logger.debug("Obdržena POST žádost k vytvoření objednávky.")

        form = OrderForm(request.POST)
        if form.is_valid():
            logger.debug("Formulář je platný, pokračuji.")

            order = form.save(commit=False)

            if not cart:
                logger.warning("Košík je prázdný, objednávka nebude vytvořena.")
                return render(request, 'checkout.html', {
                    'form': form,
                    'cart': cart,
                    'products_dict': products_dict,
                    'error': "Váš košík je prázdný.",
                })

            try:
                order.total_price = sum(products_dict[pid].price * qty for pid, qty in cart.items())
            except KeyError:
                logger.error("Chyba při načítání produktů!", exc_info=True)
                return render(request, 'checkout.html', {
                    'form': form,
                    'cart': cart,
                    'products_dict': products_dict,
                    'error': "Chyba při načítání produktů. Zkuste to znovu.",
                })

            default_status, _ = OrderStatus.objects.get_or_create(name="Nová")
            order.status = default_status
            order.save()
            logger.debug(f"Objednávka {order.id} byla uložena.")

            # Uložit produkty do objednávky
            for product_id, quantity in cart.items():
                if product_id in products_dict:
                    product = products_dict[product_id]
                    OrderItem.objects.create(order=order, product=product, quantity=quantity, price=product.price)

            logger.debug(f"Objednávka {order.id} obsahuje {len(cart)} položek.")

            # Vymazání košíku
            request.session['cart'] = {}
            request.session.modified = True

            logger.debug("Košík byl úspěšně vymazán, přesměrování na thankyou.")
            return redirect('thankyou')  # Přesměrování

        else:
            logger.warning("Formulář nebyl platný. Chyby: %s", form.errors)

    else:
        logger.debug("Byl zobrazen formulář k vytvoření objednávky.")

    return render(request, 'checkout.html', {'form': form, 'cart': cart, 'products_dict': products_dict})

def order_list(request):
    orders = Order.objects.all().order_by('-created_at')  # Seřazení od nejnovějších
    return render(request, 'order_list.html', {'orders': orders})


def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    items = order.items.all()  # Načteme všechny položky objednávky
    return render(request, 'order_detail.html', {'order': order, 'items': items})

def thankyou(request):
    return render(request, 'thankyou.html')
