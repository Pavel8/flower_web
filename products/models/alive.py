from django.db import models


class Alive(models.Model):
    # Možnosti pro Alive status
    ALIVE_CHOICES = [
        ('yes', 'Živé'),
        ('no', 'Umělé'),
    ]

    # Pole pro uložení hodnoty Alive (např. 'Živé' nebo 'Umělé')
    status = models.CharField(
        max_length=3,
        choices=ALIVE_CHOICES,
        default='yes',  # Výchozí hodnota
    )

    def __str__(self):
        return f"Alive: {self.get_status_display()}"

    def get_alive_status_display(self):
        return self.get_status_display()
