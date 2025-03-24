from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

### 🌍 COOKIES ###

def create_cookie(request):
    """Vytvoření cookie s uživatelským jménem (např. pro personalizaci)"""
    response = HttpResponse("Nastavení cookie")
    response.set_cookie("username", "john_doe", max_age=3600, secure=True, httponly=True)  # 1 hodina
    return response

def get_cookie(request):
    """Získání hodnoty cookie"""
    username = request.COOKIES.get("username", "Neznámý")
    return HttpResponse(f"Uživatel: {username}")

def delete_cookie(request):
    """Smazání cookie"""
    response = HttpResponse("Mazání cookie")
    response.delete_cookie("username")
    return response

### 🛒 KOŠÍK (COOKIES + SESSIONS) ###

def set_cart_cookie(request):
    """Uložení košíku do cookies (pro nepřihlášené uživatele)"""
    cart = request.session.get("cart", {})
    response = HttpResponse("Košík uložen do cookies")
    response.set_cookie("cart", str(cart), max_age=7*24*60*60, secure=True, httponly=True)  # Uloží košík na 7 dní
    return response

def get_cart_cookie(request):
    """Získání košíku z cookies"""
    cart = request.COOKIES.get("cart", "{}")  # Výchozí prázdný slovník
    return HttpResponse(f"Obsah košíku: {cart}")

def clear_cart_cookie(request):
    """Smazání košíku z cookies"""
    response = HttpResponse("Košík z cookies byl smazán")
    response.delete_cookie("cart")
    return response

### 🛡️ COOKIES SOUHLAS ###

def set_cookie_preference(request):
    """Uložení souhlasu s cookies (ANO / NE)"""
    response = HttpResponse("Uložení preference cookies")
    consent = request.GET.get("consent", "reject")  # Výchozí odmítnutí
    response.set_cookie("cookie_consent", consent, max_age=365*24*60*60, secure=True, httponly=True)  # 1 rok
    return response

def get_cookie_preference(request):
    """Zjištění, zda uživatel přijal cookies"""
    consent = request.COOKIES.get("cookie_consent", "unset")
    return HttpResponse(f"Souhlas s cookies: {consent}")

### 🔐 SESSIONS ###

def create_sessions(request):
    """Vytvoření session pro uživatele"""
    request.session["username"] = "john_doe"
    request.session["role"] = "admin"
    return HttpResponse("Session byla nastavena!")

def get_sessions(request):
    """Získání aktivní session"""
    username = request.session.get("username", "Neznámý uživatel")
    return HttpResponse(f"Aktivní uživatel: {username}")

def update_sessions(request):
    """Aktualizace session"""
    if "username" in request.session:
        request.session["username"] = "jane_doe"
    return HttpResponse("Session byla aktualizována!")

def delete_sessions(request):
    """Odstranění uživatele ze session (ne celý košík)"""
    if "username" in request.session:
        del request.session["username"]
    return HttpResponse("Uživatel byl odstraněn ze session!")

def clear_session(request):
    """Vymazání pouze košíku ze session, ne celé session"""
    if "cart" in request.session:
        del request.session["cart"]
    return HttpResponse("Košík byl vymazán!")

### 🛒 KOŠÍK V SESSION ###

def set_cart_session(request):
    """Uložení košíku do session"""
    cart = request.session.get("cart", {})
    request.session["cart"] = cart  # Uloží košík do session
    return HttpResponse("Košík uložen do session!")

def get_cart_session(request):
    """Získání košíku ze session"""
    cart = request.session.get("cart", {})
    return HttpResponse(f"Obsah košíku v session: {cart}")

def clear_cart_session(request):
    """Smazání košíku ze session (bez smazání celé session)"""
    if "cart" in request.session:
        del request.session["cart"]
    return HttpResponse("Košík byl smazán ze session!")
