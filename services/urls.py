from django.urls import path
from .views import ServiceListView



urlpatterns = [
    path('service-list/', ServiceListView.as_view(), name='service-list'),
]