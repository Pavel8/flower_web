from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    """Vrátí násobek hodnoty a argumentu."""
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0

@register.filter
def dict_key(dictionary, key):
    """Vrátí hodnotu z dictionary podle klíče."""
    try:
        return dictionary.get(str(key), None)
    except AttributeError:
        return None

@register.filter
def attr(obj, attr_name):
    """Vrátí hodnotu atributu objektu."""
    return getattr(obj, attr_name, None)

@register.filter
def get_item(dictionary, key):
    if isinstance(dictionary, dict):
        return dictionary.get(str(key), None)
    return None