from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from users.models import Profile

def item_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/items/<id>/<filename> 
    return 'items/{0}/{1}'.format(instance.id, filename) 

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
    count = models.IntegerField(default=1)
    available = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to=item_directory_path, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)    
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="book_created_by")    
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="book_updated_by")
    
    def __str__(self):
        return self.name    

class Order(models.Model):
    customer = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True, related_name="order_customer")
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, blank=True, null=True, related_name="order_book")
    description = models.TextField(blank=True, null=True)
    count = models.IntegerField(default=1)
    day = models.IntegerField(default=7)
    returned = models.BooleanField(default=False)
    returned_at = models.DateTimeField(blank=True, null=True)    
    created_at = models.DateTimeField(auto_now_add=True)    
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="order_created_by")    
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="order_updated_by")
    
    def __str__(self):
        return self.customer.code + "->" + self.book.name

    # def save(self, *args, **kwargs):         
    #     if self.returned == True:
    #         self.returned_at=datetime.now()
    #         self.book.available=self.book.available+1
    #     else:
    #         self.book.available=self.book.available-1
    #     super(Order, self).save(*args, **kwargs) 

class VoteOption(models.Model):
    name = models.CharField(max_length=100)    
    count = models.IntegerField(default=0)
    # valid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="vote_option_created_by")    
    
    def __str__(self):
        return self.name 

class Vote(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    selections = models.ManyToManyField(VoteOption, blank=True)        
    created_at = models.DateTimeField(auto_now_add=True)    
    updated_at = models.DateTimeField(auto_now=True)    
    
    def __str__(self):
        return self.customer.username

class VoteSelect(models.Model):
    options = models.ManyToManyField(VoteOption, blank=True)
    votes = models.ManyToManyField(Vote, blank=True)    
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="vote_select_created_by")    
    
    def __str__(self):
        return "Vote: " + str(self.created_at)