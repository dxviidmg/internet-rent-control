from django.db import models
from packages.models import Package
from clients.models import Client


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Address(models.Model):
    street_address = models.CharField(max_length=50, verbose_name='Calle y número')
    location = models.CharField(max_length=30, verbose_name='Colonia')
    city = models.CharField(max_length=50, verbose_name='Ciudad')
    zip_code = models.CharField(max_length=5, verbose_name='Codigo Postal')

    def __str__(self):
        return '{}, {}, {}, {}'.format(self.street_address, self.location, self.city, self.zip_code)

class Service(TimeStampedModel):
    status_choices = (
        (0, 'Sin iniciar'),
        (1, 'Activo'),
        (2, 'Suspención'),
        (3, 'Cancelación'),
    )

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, verbose_name='Paquete')
    status = models.IntegerField(choices=status_choices, default=0)    
    start_date_operation = models.DateField(verbose_name='Fecha de inicio de operación')
    has_late_payments = models.BooleanField(default=False)

    def __str__(self):
        return '#{}'.format(self.pk)