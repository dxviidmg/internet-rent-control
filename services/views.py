from django.views.generic.list import ListView
from .models import Service
from django.views.generic import View
from django.shortcuts import render
from clients.forms import ClientForm
from .forms import ServiceForm, AddressForm
from django.shortcuts import render, redirect


class ServiceListView(ListView):
    model = Service


class ClientAndServiceCreateView(View):
    template_name = 'services/service_create.html'
    
    def get_context(self):
        client_form = ClientForm()
        address_form = AddressForm()
        service_form = ServiceForm()
        context = {
            'client_form': client_form,
            'address_form': address_form,
            'service_form': service_form,
        }
        return context

    def get(self, request):
        return render(request, self.template_name, self.get_context())

    def post(self, request):
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

#        messages.success(request, "Actualización exitosa")
        return redirect("services:service-list")