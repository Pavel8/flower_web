from django.contrib import admin
from .models import Occasion, Product, Type, Alive

# Register your models here.
admin.site.register(Occasion)
admin.site.register(Product)
admin.site.register(Type)
admin.site.register(Alive)