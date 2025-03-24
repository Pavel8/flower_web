from django.db import models
from .order_status import OrderStatus

class Order(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    note = models.TextField(blank=True, null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, null=True, blank=True)
    payment_method = models.CharField(max_length=10, choices=[('card', 'Platba kartou'), ('cod', 'Dobírka')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Objednávka #{self.id} - {self.full_name}"
