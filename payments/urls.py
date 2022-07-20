from django.urls import path
from .views import PaymentListView, PaymentCreateView


app_name = 'payments'

urlpatterns = [
    path('payment-list/', PaymentListView.as_view(), name='payment-list'),
    path('payment-create/<int:pk>/', PaymentCreateView.as_view(), name='payment-create'),
]