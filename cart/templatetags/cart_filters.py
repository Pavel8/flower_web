from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    """Vlastní filtr pro násobení dvou čísel"""
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0


@register.filter
def get_item(dictionary, key):
    return dictionary.get(int(key))  # Zajištění přístupu k hodnotě produktu pomocí id
