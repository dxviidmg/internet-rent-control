from services.models import Service
from .models import Payment
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .forms import PaymentForm
from dateutil.relativedelta import relativedelta
from django.urls import reverse_lazy


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
        end_of_validity = service.get_end_of_validity() + relativedelta(months=form.cleaned_data['months'])
        total = service.package.price * form.cleaned_data['months']
        form.instance.service = service
        form.instance.end_of_validity = end_of_validity
        form.instance.total = total
        return super(PaymentCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('services:service-detail', kwargs={'pk': self.kwargs.get('pk')})