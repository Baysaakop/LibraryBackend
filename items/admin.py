from django.contrib import admin
from .models import Item, Category, Author, Publisher, Customer, Book, Order

admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Customer)
admin.site.register(Book)
admin.site.register(Order)
