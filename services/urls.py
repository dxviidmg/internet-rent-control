from django.urls import path
from .views import ServiceListView, ClientAddressServiceView, ServiceDetailView


app_name = 'services'

urlpatterns = [
    path('service-list/', ServiceListView.as_view(), name='service-list'),
    path('client-and-service-create/', ClientAddressServiceView.as_view(), name='service-create'),
    path('client-and-service-update/<int:pk>/', ClientAddressServiceView.as_view(), name='service-update'),
    path('service-detail/<int:pk>/', ServiceDetailView.as_view(), name='service-detail'),
]