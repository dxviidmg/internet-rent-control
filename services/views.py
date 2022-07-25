from django.views.generic.list import ListView

from payments.models import Payment
from .models import Service
from django.views.generic import View
from django.shortcuts import render
from clients.forms import ClientForm
from .forms import ServiceForm, AddressForm
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView

import io
from django.http import HttpResponse
from django.views.generic import View
import xlsxwriter
from datetime import date, datetime 


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


class PartnerReportView(View):

    def get(self, request):
        today = date.today()
        # Create an in-memory output file for the new workbook.
        output = io.BytesIO()

        # Even though the final file will be in memory the module uses temp
        # files during assembly for efficiency. To avoid this on servers that
        # don't allow temp files, for example the Google APP Engine, set the
        # 'in_memory' Workbook() constructor option as shown in the docs.
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet()

        # Get some data to write to the spreadsheet.
        services = Service.objects.filter(client__belongs_to_partner=True)
        services = sorted(services, key= lambda service: service.get_payment_day())

        data = [['Nombre', 'Telefono', 'Dirección', 'Mensualidad', 'Dia de pago', 'Pagado hasta', 'Dias de retraso']]

        for service in services:
            row = [service.client.get_full_name(), service.client.phone_number, service.address.__str__(),
            service.package.price, service.get_payment_day(), service.get_end_of_validity().strftime('%d-%m-%Y'), 
            service.calculate_days_late_payment()]
            data.append(row)


        # Write some test data.
        for row_num, columns in enumerate(data):
            for col_num, cell_data in enumerate(columns):
                worksheet.write(row_num, col_num, cell_data)

        # Close the workbook before sending the data.
        workbook.close()

        # Rewind the buffer.
        output.seek(0)

        # Set up the Http response.
        filename = 'Reporte socio ' + str(today) +'.xlsx'
        response = HttpResponse(
            output,
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename=%s' % filename

        return response