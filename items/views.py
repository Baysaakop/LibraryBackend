import csv
from datetime import datetime
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework import serializers, status, viewsets, filters
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import Category, Author, Publisher, Book, Order, VoteOption, Vote, VoteSelect
from .serializers import CategorySerializer, AuthorSerializer, PublisherSerializer, BookSerializer, OrderSerializer, VoteOptionSerializer, VoteSerializer, VoteSelectSerializer
from django.contrib.auth.models import User
from users.models import Profile

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all().order_by('-created_at')
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all().order_by('-created_at')
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class PublisherViewSet(viewsets.ModelViewSet):
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all().order_by('-created_at')
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

def isUndefined(data):
    if (data == 'undefined' or data == None or data == "null"):
        return True
    return False

# class BookFilter(FilterSet):
#     class Meta:
#         model = Book
#         fields = {
#             'name': ['exact', 'contains'],
#             'category__id': ['exact'],
#         }

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all().order_by('-created_at')
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'category__id']    

    def create(self, request, *args, **kwargs):                       
        user = Token.objects.get(key=request.data['token']).user   
        if 'file' in request.data:
            csv_file = request.data["file"]            
            lines = csv_file.split("\n")
            for line in lines:						
                fields = line.split(",")
                print(fields)
            return Response(status=status.HTTP_201_CREATED)
        else:
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
            if 'count' in request.data:
                book.count=request.data['count']  
            if 'available' in request.data:
                book.available=request.data['available']  
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
        if 'count' in request.data:
            book.count=request.data['count']              
        if 'available' in request.data:
            book.available=request.data['available']  
        if 'image' in request.data:
            book.image=request.data['image'] 
        book.save()
        serializer = BookSerializer(book)
        headers = self.get_success_headers(serializer.data)        
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)       

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all().order_by('-created_at')
    filter_backends = [filters.SearchFilter]
    search_fields = ['customer__code']

    def create(self, request, *args, **kwargs):                       
        user = Token.objects.get(key=request.data['token']).user   
        customer=Profile.objects.get(pk=int(request.data['customer']))
        book=Book.objects.get(pk=int(request.data['book']))
        order = Order.objects.create(
            customer=customer,                   
            book=book,                   
            created_by=user        
        )                      
        if 'description' in request.data:
            order.description=request.data['description']        
        if 'count' in request.data:
            order.count=request.data['count']            
        if (book.available > 0):            
            book.available=book.available-order.count
            book.save()
        else:
            return Response("Not available", status=status.HTTP_406_NOT_ACCEPTABLE)
        order.save()
        serializer = OrderSerializer(order)
        headers = self.get_success_headers(serializer.data)        
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)    

    def update(self, request, *args, **kwargs):                         
        order = self.get_object()                 
        user = Token.objects.get(key=request.data['token']).user
        order.updated_by=user
        # if 'customer' in request.data:
        #     order.customer=Profile.objects.get(pk=int(request.data['customer']))  
        # if 'book' in request.data:
        #     order.book=Book.objects.get(pk=int(request.data['book']))
        # if 'description' in request.data:
        #     order.description=request.data['description']        
        # if 'count' in request.data:
        #     order.count=request.data['count'] 
        if 'returned' in request.data:
            if request.data['returned'] == 'True':
                order.returned = True
                order.returned_at = datetime.now()
                order.book.available=order.book.available+order.count
                order.book.save()
        order.save()
        serializer = OrderSerializer(order)
        headers = self.get_success_headers(serializer.data)        
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)

class VoteOptionViewSet(viewsets.ModelViewSet):
    serializer_class = VoteOptionSerializer
    queryset = VoteOption.objects.all().order_by('-count')
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def create(self, request, *args, **kwargs):                       
        user = Token.objects.get(key=request.data['token']).user   
        name = request.data['name']
        if (VoteOption.objects.filter(name=name).count() > 0):
            return Response("Not available", status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            option = VoteOption.objects.create(                 
                name=name,
                count=1,
                created_by=user        
            )                      
            option.save()
            vote, created = Vote.objects.get_or_create(customer=user)
            vote.selections.add(option)
            vote.save()
            select = VoteSelect.objects.latest('created_at')            
            select.options.add(option)
            select.votes.add(vote)
            serializer = VoteOptionSerializer(option)
            headers = self.get_success_headers(serializer.data)        
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers) 

class VoteViewSet(viewsets.ModelViewSet):
    serializer_class = VoteSerializer
    queryset = Vote.objects.all().order_by('-created_at')
    filter_backends = [filters.SearchFilter]
    search_fields = ['selection__id']

    def create(self, request, *args, **kwargs):                       
        user = Token.objects.get(key=request.data['token']).user   
        option = VoteOption.objects.get(id=int(request.data['option']))
        vote = Vote.objects.create(                 
            customer=user            
        )                  
        # if option in request.data:
        #     arr = str(request.data['option']).split(',')
        #     for item in arr:
        vote.selections.add(option)                            
        vote.save()
        select = VoteSelect.objects.latest('created_at')                   
        select.votes.add(vote)
        serializer = VoteSerializer(vote)
        headers = self.get_success_headers(serializer.data)        
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers) 

    def update(self, request, *args, **kwargs):                         
        vote = self.get_object()                 
        user = Token.objects.get(key=request.data['token']).user   
        option = VoteOption.objects.get(id=int(request.data['option']))
        if option in vote.selections:
            vote.selections.remove(option)
        else:
            vote.selections.add(option)
        # vote.sele
        # if 'options' in request.data:
        #     arr = str(request.data['options']).split(',')
        #     for item in arr:
        #         vote.selections.add(int(item))   
        vote.save()
        serializer = OrderSerializer(vote)
        headers = self.get_success_headers(serializer.data)        
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)

class VoteSelectViewSet(viewsets.ModelViewSet):
    serializer_class = VoteSelectSerializer
    queryset = VoteSelect.objects.all().order_by('-created_at')

    def create(self, request, *args, **kwargs):                       
        user = Token.objects.get(key=request.data['token']).user   
        select = VoteSelect.objects.create(                 
            created_by=user        
        )                      
        select.save()
        serializer = VoteSelectSerializer(select)
        headers = self.get_success_headers(serializer.data)        
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)        