import xlrd
import datetime
from clients.models import Client
from services.models import Address, Service
from packages.models import Package


def run(): 
    wb = xlrd.open_workbook('scripts/Clientes Internet 21 Julio 2022.xlsx')
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)
    
    for i in range(1, sheet.nrows):
        full_name = sheet.cell_value(i, 0)
        full_name_split = full_name.split()

        data_client = dict()
        data_client['first_name'] = full_name_split[0]

        try:
            data_client['last_name'] = full_name_split[1]
        except:
            pass

        try:
            data_client['second_last_name'] = full_name_split[2]
        except:
            pass
        
#        data_client['belongs_to_partner'] = True
        belongs_to = sheet.cell_value(i, 6)
        if belongs_to == 'SOCIO':
            data_client['belongs_to_partner'] = True

        client, client_create = Client.objects.get_or_create(**data_client)

        data_address = dict()
        data_address['street_address'] = sheet.cell_value(i, 1)
        data_address['location'] = sheet.cell_value(i, 2)
        data_address['city'] = sheet.cell_value(i, 3)        

        address, address_create = Address.objects.get_or_create(**data_address)

        data_package = dict()
        price = int(sheet.cell_value(i, 4))
        data_package['price'] = price

        if price <= 250:
            data_package['bandwidth'] = 2
        elif price <= 350:
            data_package['bandwidth'] = 3
        else:
            data_package['bandwidth'] = 10

        package, package_create = Package.objects.get_or_create(**data_package)

        start_date_operation = datetime.datetime(2022, 7, int(sheet.cell_value(i, 5)))

        data_service = dict()
        data_service['client'] = client
        data_service['address'] = address
        data_service['package'] = package
        data_service['start_date_operation'] = start_date_operation

        Service.objects.get_or_create(**data_service)