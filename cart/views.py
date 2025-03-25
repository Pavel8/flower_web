from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from products.models.product import Product
from django.shortcuts import render
from django.http import JsonResponse
from products.models import Product


from django.shortcuts import redirect, get_object_or_404
from products.models.product import Product
from django.http import HttpResponse
import json

def cart_add(request, product_id):
    """Přidání produktu do košíku bez zprávy."""
    is_authenticated = request.user.is_authenticated

    # Načíst košík (session pro přihlášené, cookies pro anonymní)
    if is_authenticated:
        cart = request.session.get("cart", {})
    else:
        cart = request.COOKIES.get("cart", "{}")
        try:
            cart = json.loads(cart)
        except json.JSONDecodeError:
            cart = {}

        # Ujisti se, že product_id je řetězec
    product_id = str(product_id)

    # Přidání produktu do košíku
    if product_id in cart:
        cart[product_id] += 1  # Zvyšte množství
    else:
        cart[product_id] = 1  # Přidejte první kus

    # Uložit zpět
    if is_authenticated:
        request.session["cart"] = cart
        request.session.modified = True
    else:
        response = HttpResponse(status=204)  # Odpověď bez obsahu
        response.set_cookie("cart", json.dumps(cart), max_age=7 * 24 * 60 * 60, secure=False, httponly=False)
        return response

    return HttpResponse(status=204)  # Odpověď pro přihlášené uživatele


def cart_detail(request):
    cart = request.session.get('cart', {})
    cart_items = []

    # Načítání produktů podle jejich ID z košíku
    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total_price': product.price * quantity  # Celková cena
        })

    total_price = sum(item['total_price'] for item in cart_items)

    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})


def cart_remove(request, product_id):
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
        messages.success(request, "Produkt byl odstraněn z košíku.")

    return redirect('cart')  # Uprav podle názvu tvé stránky košíku

from django.http import JsonResponse

def debug_cart(request):
    """Vrátí JSON odpověď s obsahem košíku pro debugování."""
    cart_session = request.session.get("cart", {})
    cart_cookie = request.COOKIES.get("cart", "{}")  # Cookies jsou string!

    return JsonResponse({
        "cart_session": cart_session,
        "cart_cookie": cart_cookie
    })

from django.shortcuts import render

def cart_view(request):
    """Zobrazení košíku."""
    is_authenticated = request.user.is_authenticated

    # Získání košíku z session nebo cookies
    if is_authenticated:
        cart = request.session.get("cart", {})
    else:
        import json
        cart = request.COOKIES.get("cart", "{}")
        try:
            cart = json.loads(cart)
        except json.JSONDecodeError:
            cart = {}

    # Načítání produktů podle jejich ID
    cart_items = []
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total_price': product.price * quantity,  # Celková cena
        })

    total_price = sum(item['total_price'] for item in cart_items)

    # Předání položek do šablony
    return render(request, "cart.html", {"cart_items": cart_items, "total_price": total_price})


def checkout(request):
    """Zobrazí obsah košíku na stránce checkout."""
    cart = request.session.get("cart", {})

    # Ujisti se, že klíče v cart jsou stringy
    cart = {str(k): v for k, v in cart.items()}

    # Načtení všech produktů, které jsou v košíku
    product_ids = cart.keys()
    products = Product.objects.filter(id__in=product_ids)

    # Vytvoření slovníku {id: product_object}
    products_dict = {str(product.id): product for product in products}

    # Výpočet celkové ceny s podrobným výpisem pro ladění
    total_price = 0
    for product_id, quantity in cart.items():
        product = products_dict.get(str(product_id))
        if product:
            item_total = product.price * quantity
            total_price += item_total
            print(
                f"Product {product.title} (ID: {product.id}) - Quantity: {quantity}, Price: {product.price}, Total: {item_total}")
        else:
            print(f"Product with ID {product_id} not found!")

    print("Total price:", total_price)  # Debug: Tiskne celkovou cenu do konzole

    return render(request, "checkout.html", {
        "cart": cart,
        "products": products_dict,
        "total_price": total_price  # Posíláme do šablony
    })

def cart_add_quantity(request, product_id):
    """Přidání 1 kusu produktu do košíku."""
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        cart[str(product_id)] += 1  # Zvyšujeme množství o 1
    else:
        cart[str(product_id)] = 1  # Pokud není v košíku, přidáme 1 kus

    request.session['cart'] = cart
    messages.success(request, "Produkt byl přidán do košíku.")

    return redirect('cart')  # Opravené přesměrování na správnou URL 'cart'


def cart_remove_quantity(request, product_id):
    """Odebrání 1 kusu produktu z košíku."""
    cart = request.session.get('cart', {})

    if str(product_id) in cart and cart[str(product_id)] > 1:
        cart[str(product_id)] -= 1  # Snižujeme množství o 1
        request.session['cart'] = cart
        messages.success(request, "Množství produktu bylo sníženo.")

    return redirect('cart')  # Opravené přesměrování na správnou URL 'cart'
