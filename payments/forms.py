from django import forms
from .models import Payment
from services.models import Service
from dateutil.relativedelta import relativedelta


class PaymentForm(forms.ModelForm):
    months = forms.IntegerField()

    class Meta:
        model = Payment
        fields = ['months']