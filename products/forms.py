from django import forms
from .models import Product, Occasion, Alive

class ProductForm(forms.ModelForm):
    # Změna: Explicitní nastavení zobrazení pro ManyToManyField "occasion"
    occasion = forms.ModelMultipleChoiceField(
        queryset=Occasion.objects.all(),  # Vybere všechny existující příležitosti
        widget=forms.CheckboxSelectMultiple,  # Zobrazí jako checkboxy (můžeš změnit widget dle potřeby)
        required=False,  # Pole není povinné
    )

    # Změna: Explicitní nastavení zobrazení pro ForeignKey "alive"
    alive = forms.ModelChoiceField(
        queryset=Alive.objects.all(),
        widget=forms.RadioSelect,  # Zobrazí jako radio buttony
        required=False,  # Pole není povinné
    )

    class Meta:
        model = Product
        fields = "__all__"  # Zde lze také explicitně vypsat pouze požadovaná pole
