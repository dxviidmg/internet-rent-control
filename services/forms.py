from .models import Address, Service
from django import forms


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        exclude = ['client', 'address']

        widgets = {
            'start_date_operation': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                  }),
                }