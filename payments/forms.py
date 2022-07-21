from django import forms
from .models import Payment
from services.models import Service
from dateutil.relativedelta import relativedelta


class PaymentForm(forms.ModelForm):

    class Meta:
        model = Payment
        fields = ['months']