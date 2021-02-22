from django.core.management.base import BaseCommand
from items.models import Book, Category, Author

class Command(BaseCommand):
    def handle(self, *args, **kwargs):                       
        Author.objects.all().delete()
        Category.objects.all().delete()
        Book.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Deleted all data'))