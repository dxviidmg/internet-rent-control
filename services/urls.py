from django.urls import path
from .views import ServiceListView, ClientAndServiceCreateView## AddressAndServiceCreateView


app_name = 'services'

urlpatterns = [
    path('service-list/', ServiceListView.as_view(), name='service-list'),
    path('client-and-service-create/', ClientAndServiceCreateView.as_view(), name='service-create'),
#    path('service-create-2/', AddressAndServiceCreateView.as_view(), name='service-create-2'),
]