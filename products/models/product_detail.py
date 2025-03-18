from django.db import models
from .product import Product

class ProductDetail(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    summary = models.TextField()
    idcode = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return f"Details for {self.product.title}"