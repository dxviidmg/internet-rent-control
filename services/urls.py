from django.urls import path
from .views import ServiceListView, ClientAndServiceCreateView, ServiceDetailView


app_name = 'services'

urlpatterns = [
    path('service-list/', ServiceListView.as_view(), name='service-list'),
    path('client-and-service-create/', ClientAndServiceCreateView.as_view(), name='service-create'),
    path('service-detail/<int:pk>/', ServiceDetailView.as_view(), name='service-detail'),
]