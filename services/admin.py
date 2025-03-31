from django.contrib import admin
from django.db import models
from django.forms import Textarea
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 10, 'cols': 80})},
    }

admin.site.register(Service, ServiceAdmin)