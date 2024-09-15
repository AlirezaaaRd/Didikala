from django import forms
from .models import Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['name', 'phone_number', 'state', 'city', 'postal_code', 'description']