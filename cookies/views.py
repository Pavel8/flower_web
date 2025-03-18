from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def create_cookie(request):
    """Vytvoření cookie s uživatelským jménem."""
    response = HttpResponse("Nastavení cookie")
    response.set_cookie("username", "john_doe", max_age=3600)  # Expirace 1 hodina
    return response

def get_cookie(request):
    """Získání hodnoty cookie."""
    username = request.COOKIES.get("username", "Neznámý")
    return HttpResponse(f"Používateľ: {username}")

def delete_cookie(request):
    """Smazání cookie."""
    response = HttpResponse("Mazání cookie")
    response.delete_cookie("username")
    return response

@login_required
def swap_cookie(request):
    """Přepnutí režimu mezi světlým a tmavým (light/dark)."""
    mode = request.COOKIES.get("mode", "dark")
    mode = "light" if mode == "dark" else "dark"
    response = redirect("cookies")
    response.set_cookie("mode", mode, expires=None)
    return response

def set_cookie_preference(request):
    """Uložení uživatelského souhlasu s cookies."""
    response = HttpResponse("Uložení preference cookies")
    consent = request.GET.get("consent", "reject")  # Přijato nebo odmítnuto
    response.set_cookie("cookie_consent", consent, max_age=365*24*60*60)  # 1 rok
    return response

def get_cookie_preference(request):
    """Zjištění, zda uživatel přijal cookies."""
    consent = request.COOKIES.get("cookie_consent", "unset")
    return HttpResponse(f"Souhlas s cookies: {consent}")
