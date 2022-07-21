from clients.models import Client
from services.models import Service
from django.db.models import Sum


def calculate_comision():
    clients = Client.objects.filter(belongs_to_partner=False)
    services = Service.objects.filter(client__in=clients)
    package__price__sum = services.aggregate(Sum('package__price'))['package__price__sum']
    comision = package__price__sum * .1
    print('Comision:', comision)

def run():
    calculate_comision()

