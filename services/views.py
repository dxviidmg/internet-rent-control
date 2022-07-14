from django.views.generic.list import ListView
from .models import Service


class ServiceListView(ListView):
    model = Service