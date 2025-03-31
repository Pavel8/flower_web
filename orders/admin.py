from django.contrib import admin
from .models import Order, OrderItem, OrderStatus

# Inline pro zobrazení položek objednávky v administraci
class OrderItemInline(admin.TabularInline):
    model = OrderItem  # Zde specifikujeme model pro položky objednávky
    extra = 1  # Počet prázdných řádků pro přidání nových položek

# Administrace pro objednávky
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'total_price', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('full_name', 'email', 'phone')
    readonly_fields = ('created_at',)
    inlines = [OrderItemInline]  # Přidáme inline pro položky objednávky

# Administrace pro položky objednávky
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price')

# Administrace pro statusy objednávek
@admin.register(OrderStatus)
class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ('name',)
