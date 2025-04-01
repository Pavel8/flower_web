from django import forms

class StaffLoginForm(forms.Form):
    username = forms.CharField(label="Uživatelské jméno")
    password = forms.CharField(widget=forms.PasswordInput, label="Heslo")
