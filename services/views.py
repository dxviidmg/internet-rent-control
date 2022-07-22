from django.views.generic.list import ListView

from payments.models import Payment
from .models import Service
from django.views.generic import View
from django.shortcuts import render
from clients.forms import ClientForm
from .forms import ServiceForm, AddressForm
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView


class ServiceListView(ListView):
    model = Service


class ClientAddressServiceView(View):
    template_name = 'services/service_form.html'
    def get(self, request, pk=None):

        if pk:
            service= Service.objects.get(pk=self.kwargs['pk'])
            client_form = ClientForm(instance=service.client)
            address_form = AddressForm(instance=service.address)
            service_form = ServiceForm(instance=service)
        else:
            service = None
            client_form = ClientForm()
            address_form = AddressForm()
            service_form = ServiceForm()

        context = {
            'service': service,
            'client_form': client_form,
            'address_form': address_form,
            'service_form': service_form,
        }

        return render(request, self.template_name, context)

    def post(self, request, pk=None):
        if pk:
            service= Service.objects.get(pk=self.kwargs['pk'])
            client_form = ClientForm(request.POST, instance=service.client)
            address_form = AddressForm(request.POST, instance=service.address)
            service_form = ServiceForm(request.POST, instance=service)
        else:
            client_form = ClientForm(request.POST)
            address_form = AddressForm(request.POST)
            service_form = ServiceForm(request.POST)

        if client_form.is_valid() and address_form.is_valid() and service_form.is_valid():
            client = client_form.save()
            address = address_form.save()
            service = service_form.save(commit=False)
            service.client = client
            service.address = address
            service.save()

        if pk:
            return redirect("services:service-detail", pk)
        return redirect("services:service-list")


class ServiceDetailView(DetailView):
    model = Service

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(*args, **kwargs)
        data['object_list'] = Payment.objects.filter(service_id=self.kwargs['pk'])
        return data
