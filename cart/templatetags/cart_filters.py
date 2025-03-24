from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    """Vlastní filtr pro násobení dvou čísel"""
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0
