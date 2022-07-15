from .models import Address, Service
from django import forms


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        exclude = ['client', 'address', 'status', 'has_late_payments']