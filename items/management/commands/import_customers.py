from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from items.models import Customer
from datetime import date
import csv

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            'file_name', type=str, help='The txt file that contains the customers'
        )

    def handle(self, *args, **kwargs):
        file_name = kwargs['file_name']
        with open(f'{file_name}.csv', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:                
                c_name = row[0]
                c_code = row[1]
                c_mobile = row[2]                
                c_birthday = row[3]                

                customer = Customer.objects.create(
                    name = c_name,
                    code = c_code,                                       
                    mobile = c_mobile,
                    birthday = c_birthday
                )
                
                customer.save()                                                  
                
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))