from django.db import models
from packages.models import Package
from clients.models import Client
from datetime import date 

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Address(models.Model):
    street_address = models.CharField(max_length=50, verbose_name='Calle y número')
    location = models.CharField(max_length=30, verbose_name='Colonia')
    city = models.CharField(max_length=50, verbose_name='Ciudad')
    
    def __str__(self):
        return '{}, {}, {}'.format(self.street_address, self.location, self.city)

class Service(TimeStampedModel):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, verbose_name='Paquete')
    start_date_operation = models.DateField(verbose_name='Fecha de inicio de operación')

    def __str__(self):
        return '#{}'.format(self.pk)

    def get_end_of_validity(self):
        payments = self.payments.all().order_by('end_of_validity')
        if payments.exists():
            return payments.last().end_of_validity
        return self.start_date_operation

    def has_late_payments(self):
        today = date.today()
        if today < self.get_end_of_validity():
            return False
        return True

