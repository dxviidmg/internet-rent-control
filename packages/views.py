from .models import Package
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
#from .forms import PaymentForm
from dateutil.relativedelta import relativedelta
from django.urls import reverse_lazy


class PackageListView(ListView):
    model = Package


class PackageCreateView(CreateView):
    model = Package
    fields = '__all__'
    success_url = reverse_lazy('packages:package-list')