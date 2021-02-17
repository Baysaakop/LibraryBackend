from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import Item, Category, Author, Publisher, Customer, Book, Order
from .serializers import ItemSerializer, CategorySerializer, AuthorSerializer, PublisherSerializer, CustomerSerializer, BookSerializer, OrderSerializer
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class PublisherViewSet(viewsets.ModelViewSet):
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

def isUndefined(data):
    if (data == 'undefined' or data == None or data == "null"):
        return True
    return False

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def create(self, request, *args, **kwargs):                       
        user = Token.objects.get(key=request.data['token']).user   
        book = Book.objects.create(
            name=request.data['name'],                   
            created_by=user        
        )                      
        if 'code' in request.data:
            book.code=request.data['code']
        if 'description' in request.data:
            book.description=request.data['description']
        if 'category' in request.data:
            arr = str(request.data['category']).split(',')
            for item in arr:
                book.category.add(int(item))
        if 'author' in request.data:
            arr = str(request.data['author']).split(',')
            for item in arr:
                book.author.add(int(item))
        if 'publisher' in request.data:
            arr = str(request.data['publisher']).split(',')
            for item in arr:
                book.publisher.add(int(item))
        if 'published_at' in request.data:
            book.published_at=request.data['published_at']
        if 'pages' in request.data:
            book.pages=request.data['pages']
        if 'height' in request.data:
            book.height=request.data['height']
        if 'width' in request.data:
            book.width=request.data['width']
        if 'depth' in request.data:
            book.depth=request.data['depth']
        if 'weight' in request.data:
            book.weight=request.data['weight']        
        if 'count' in request.data:
            book.count=request.data['count']  
        if 'available' in request.data:
            book.available=request.data['available']  
        if 'price' in request.data:
            book.price=request.data['price'] 
        if 'image' in request.data:
            book.image=request.data['image']  
        book.save()
        serializer = BookSerializer(book)
        headers = self.get_success_headers(serializer.data)        
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)    

    def update(self, request, *args, **kwargs):                         
        book = self.get_object()                 
        user = Token.objects.get(key=request.data['token']).user
        book.updated_by=user
        if 'name' in request.data:
            book.name=request.data['name']
        if 'code' in request.data:
            book.code=request.data['code']
        if 'description' in request.data:
            book.description=request.data['description']
        if 'category' in request.data:          
            book.category.clear()  
            arr = str(request.data['category']).split(',')
            for item in arr:
                check = item.isnumeric()
                if check == True:
                    book.category.add(int(item))                
        if 'author' in request.data:
            book.author.clear()  
            arr = str(request.data['author']).split(',')
            for item in arr:
                check = item.isnumeric()
                if check == True:
                    book.author.add(int(item))                
        if 'publisher' in request.data:
            book.publisher.clear()  
            arr = str(request.data['publisher']).split(',')            
            for item in arr:
                check = item.isnumeric()
                if check == True:
                    book.publisher.add(int(item))                
        if 'published_at' in request.data:
            book.published_at=request.data['published_at']
        if 'pages' in request.data:
            book.pages=request.data['pages']
        if 'height' in request.data:
            book.height=request.data['height']
        if 'width' in request.data:
            book.width=request.data['width']
        if 'depth' in request.data:
            book.depth=request.data['depth']
        if 'weight' in request.data:
            book.weight=request.data['weight']        
        if 'count' in request.data:
            book.count=request.data['count']              
        if 'available' in request.data:
            book.available=request.data['available']  
        if 'price' in request.data:
            book.price=request.data['price'] 
        if 'image' in request.data:
            book.image=request.data['image'] 
        book.save()
        serializer = BookSerializer(book)
        headers = self.get_success_headers(serializer.data)        
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)       

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def create(self, request, *args, **kwargs):                       
        user = Token.objects.get(key=request.data['token']).user   
        order = Order.objects.create(
            customer=Customer.objects.get(pk=int(request.data['customer'])),                   
            book=Book.objects.get(pk=int(request.data['book'])),                   
            created_by=user        
        )                      
        if 'description' in request.data:
            order.description=request.data['description']        
        if 'count' in request.data:
            order.count=request.data['count']
        if 'day' in request.data:
            order.day=request.data['day']        
        order.save()
        serializer = OrderSerializer(order)
        headers = self.get_success_headers(serializer.data)        
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)    

    def update(self, request, *args, **kwargs):                         
        order = self.get_object()                 
        user = Token.objects.get(key=request.data['token']).user
        order.updated_by=user
        if 'customer' in request.data:
            order.customer=Customer.objects.get(pk=int(request.data['customer']))  
        if 'book' in request.data:
            order.book=Book.objects.get(pk=int(request.data['book']))
        if 'description' in request.data:
            order.description=request.data['description']        
        if 'count' in request.data:
            order.count=request.data['count'] 
        if 'day' in request.data:
            order.day=request.data['day'] 
        order.save()
        serializer = OrderSerializer(order)
        headers = self.get_success_headers(serializer.data)        
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)