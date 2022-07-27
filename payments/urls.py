from django.urls import path
from .  import views


app_name = 'payments'

urlpatterns = [
    path('payment-list/', views.PaymentListView.as_view(), name='payment-list'),
    path('payment-create/<int:pk>/', views.PaymentCreateView.as_view(), name='payment-create'),
    path('payment-delete/<int:pk>/', views.PaymentDeleteView.as_view(), name='payment-delete'),
    path('payments-sum-by-month/', views.PaymentsSumByMonthListView.as_view(), name='payments-sum-by-month-list'),
]