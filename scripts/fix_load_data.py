from services.models import Service, Address


def fix_address():
    services = Service.objects.filter(address__street_address='')
    for service in services:
        data_address = dict()
        data_address['street_address'] = service.pk
        data_address['location'] = service.address.location
        data_address['city'] = service.address.city

        address, address_created = Address.objects.get_or_create(**data_address)

        service.address = address
        service.save()

    services.delete()

def run():  
    fix_address()
