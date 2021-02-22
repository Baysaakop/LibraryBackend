from django.contrib import admin
from .models import Category, Author, Publisher, Book, Order, VoteOption, Vote, VoteSelect

admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Order)
admin.site.register(VoteOption)
admin.site.register(Vote)
admin.site.register(VoteSelect)
