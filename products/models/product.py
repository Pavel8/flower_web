from django.db import models
from .type import Type
from .occasion import Occasion
from .alive import Alive
import datetime

class Product(models.Model):
    COLOR_CHOICES = [
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('yellow', 'Yellow'),
        ('white', 'White'),
        ('pink', 'Pink'),
        ('purple', 'Purple'),
        ('orange', 'Orange'),
        # Přidej další barvy dle potřeby
    ]
    title = models.CharField(max_length=255)
    short_description = models.TextField(blank=True)
    description = models.TextField(blank=True)  # Popis produktu
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    discount = models.DecimalField(max_digits=5, decimal_places=2, null=True,
                                   blank=True)  # Změna: Přidána sleva (může představovat procentuální nebo pevnou hodnotu)
    stock_status = models.BooleanField(default=True)  # Skladem / Dostupnost
    is_active = models.BooleanField(default=True)  # Aktivní produkt
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True, blank=True)  # Typ produktu
    occasion = models.ManyToManyField(Occasion)  # Příležitost
    alive = models.ForeignKey(Alive, on_delete=models.SET_NULL, null=True, blank=True)  # Živý/Umělý
    color = models.CharField(max_length=50, choices=COLOR_CHOICES, default='red')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Změna: Datum poslední aktualizace

    # Hlavní obrázek (obrázky zůstávají ve složce media)
    main_image = models.ImageField(upload_to='products/images/', null=True, blank=True)

    # Doplňující obrázky (maximum 5)
    additional_image_1 = models.ImageField(upload_to='products/images/', null=True, blank=True)
    additional_image_2 = models.ImageField(upload_to='products/images/', null=True, blank=True)
    additional_image_3 = models.ImageField(upload_to='products/images/', null=True, blank=True)
    additional_image_4 = models.ImageField(upload_to='products/images/', null=True, blank=True)
    additional_image_5 = models.ImageField(upload_to='products/images/', null=True, blank=True)

    def __str__(self):
        alive_status = self.alive.get_alive_status_display() if self.alive else "Not Specified"
        return f"{self.title} ({self.type}) - Alive: {alive_status}"
