from django.db import models
from .type import Type
from .occasion import Occasion
from .alive import Alive


class Product(models.Model):
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    occasion = models.ManyToManyField(Occasion)
    alive = models.ForeignKey(Alive, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        alive_status = self.alive.get_alive_status_display() if self.alive else "Not Specified"
        return f"{self.title} ({self.type}) - Alive: {alive_status}"
