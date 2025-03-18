from django import forms
from .models import Product, Occasion, Alive


class ProductForm(forms.ModelForm):
    # Změna pro správné zobrazení "ManyToManyField"
    occasion = forms.ModelMultipleChoiceField(
        queryset=Occasion.objects.all(),  # Vyber všechny existující příležitosti
        widget=forms.CheckboxSelectMultiple,  # Můžeš použít i jiný widget, např. SelectMultiple
        required=False,  # Pokud je to volitelné
    )

    alive = forms.ModelChoiceField(
        queryset=Alive.objects.all(),
        widget=forms.RadioSelect,  # Tohle vykreslí radio buttony
        required=False,  # Pokud to není povinné
    )
    class Meta:
        model = Product
        fields = "__all__"
