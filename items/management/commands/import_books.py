from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from items.models import Book, Category, Author
from datetime import date
import csv

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            'file_name', type=str, help='The txt file that contains the books'
        )

    def handle(self, *args, **kwargs):
        file_name = kwargs['file_name']
        with open(f'{file_name}.csv', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:                
                b_name = row[0]
                b_author = row[1]
                b_published_at = row[2]                
                b_category = row[3]
                b_count = row[4]                                           

                book = Book.objects.create(
                    name = b_name,                                       
                )

                if (str(b_published_at).isnumeric() == True):
                    book.published_at = int(b_published_at)                

                if (str(b_count).isnumeric() == True):
                    book.count = int(b_count)
                    book.available = int(b_count)                                              

                book.save()                                  

                authorlist = b_author.split(',')
                for a in authorlist:
                    if (a != None and a != ''):
                        author = Author.objects.get_or_create(name=a.strip())                                         
                        book.author.add(Author.objects.get(name=a.strip()))                         
                
                categorylist = b_category.split(',')
                for c in categorylist:
                    if (c != None and c != ''):
                        category = Category.objects.get_or_create(name=c.strip())                     
                        book.category.add(Category.objects.get(name=c.strip()))                       
                
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))