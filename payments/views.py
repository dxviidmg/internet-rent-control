from services.models import Service
from .models import Payment
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView
from .forms import PaymentForm
from dateutil.relativedelta import relativedelta
from django.urls import reverse_lazy
from django.views.generic import View
from django.shortcuts import render
from django.db.models import Sum


class PaymentListView(ListView):
    model = Payment

class PaymentCreateView(CreateView):
    model = Payment
    form_class = PaymentForm

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['service'] = Service.objects.get(pk=self.kwargs['pk'])
        return data

    def form_valid(self, form):
        service = Service.objects.get(id=self.kwargs.get('pk'))
        months = int(form.cleaned_data['months'])
        end_of_validity = service.get_end_of_validity() + relativedelta(months=months)
        total = service.package.price * months
        form.instance.service = service
        form.instance.end_of_validity = end_of_validity
        form.instance.total = total
        return super(PaymentCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('services:service-detail', kwargs={'pk': self.kwargs.get('pk')})


class PaymentDeleteView(DeleteView):
    model = Payment
    
    def get_success_url(self):
        return reverse_lazy('services:service-detail', kwargs={'pk': self.object.service.pk})


class PaymentsSumByMonthListView(View):
    template_name = 'payments/payments_sum.html'
    def get(self, request):
        payments = Payment.objects.all()
        months_and_years = payments.values_list('created_at__month', 'created_at__year').distinct()

        payments_sum = dict()
        for month_and_year in months_and_years:
            month = month_and_year[0]
            year = month_and_year[1]
            payments_by_month = payments.filter(created_at__month=month, created_at__year=year)
            total__sum = payments_by_month.aggregate(Sum('total'))['total__sum']
            
            payments_sum[month_and_year] = total__sum


        context={
            'payments_sum': payments_sum
        }
        return render(request, self.template_name, context)




