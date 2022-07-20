from django.shortcuts import render
from .models import Payment
from django.views.generic.list import ListView


class PaymentListView(ListView):
    model = Payment