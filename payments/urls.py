from django.urls import path
from .views import PaymentListView


app_name = 'payments'

urlpatterns = [
    path('payment-list/', PaymentListView.as_view(), name='payment-list'),
]