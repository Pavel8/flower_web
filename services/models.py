from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="Název služby")
    main_image = models.ImageField(upload_to="services/main/", verbose_name="Hlavní obrázek")
    image = models.ImageField(upload_to="services/", verbose_name="Vedlejší obrázek", blank=True, null=True)
    short_description = models.TextField(max_length=300, verbose_name="Krátký popis")  # max 300 znaků
    description = models.TextField()  # Prostý text bez formátování

    def __str__(self):
        return self.title