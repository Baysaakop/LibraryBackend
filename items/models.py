from django.db import models
from django.contrib.auth.models import User

def item_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/items/<id>/<filename> 
    return 'items/{0}/{1}'.format(instance.id, filename) 

class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=item_directory_path, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="item_created_by")
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="item_updated_by")

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="category_created_by")
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="category_updated_by")
    
    def __str__(self):
        return self.name    

class Author(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="author_created_by")
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="author_updated_by")
    
    def __str__(self):
        return self.name    

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="publisher_created_by")
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="publisher_updated_by")
    
    def __str__(self):
        return self.name    
    
class Book(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    category = models.ManyToManyField(Category, blank=True)
    author = models.ManyToManyField(Author, blank=True)
    publisher = models.ManyToManyField(Publisher, blank=True)
    published_at = models.IntegerField(default=0)
    pages = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    depth = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    available = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to=item_directory_path, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)    
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="book_created_by")    
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="book_updated_by")
    
    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    birthday = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="customer_created_by")
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="customer_updated_by")
    
    def __str__(self):
        return self.name  

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True, related_name="order_customer")
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, blank=True, null=True, related_name="order_book")
    description = models.TextField(blank=True, null=True)
    count = models.IntegerField(default=1)
    day = models.IntegerField(default=7)
    created_at = models.DateTimeField(auto_now_add=True)    
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="order_created_by")    
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="order_updated_by")
    
    def __str__(self):
        return str(self.id)