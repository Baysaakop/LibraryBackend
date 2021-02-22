from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Author, Category, Publisher, Book, Order, VoteOption, Vote, VoteSelect
from users.serializers import UserSerializer, ProfileSerializer
from users.models import Profile

class AuthorSerializer(serializers.ModelSerializer):     
    token = serializers.CharField(write_only=True)     
    created_by = UserSerializer(read_only=True)
    updated_by = UserSerializer(read_only=True)
    class Meta:
        model = Author
        fields = (
            'id', 'name', 'description', 'created_by', 'created_at', 'updated_by', 'updated_at', 'token'           
        ) 

    def create(self, validated_data):                
        user = Token.objects.get(key=validated_data['token']).user                
        author = Author(
            name = validated_data['name'],
            description = validated_data['description'],
            created_by = user 
        )
        author.save()
        return author

    def update(self, instance, validated_data):                
        user = Token.objects.get(key=validated_data['token']).user   
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)     
        instance.updated_by = user
        instance.save()
        return instance

class CategorySerializer(serializers.ModelSerializer):     
    token = serializers.CharField(write_only=True)     
    created_by = UserSerializer(read_only=True)
    updated_by = UserSerializer(read_only=True)
    class Meta:
        model = Category
        fields = (
            'id', 'name', 'description', 'created_by', 'created_at', 'updated_by', 'updated_at', 'token'            
        )

    def create(self, validated_data):                
        user = Token.objects.get(key=validated_data['token']).user                
        category = Category(
            name = validated_data['name'],
            description = validated_data['description'],
            created_by = user 
        )
        category.save()
        return category

    def update(self, instance, validated_data):                
        user = Token.objects.get(key=validated_data['token']).user   
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)     
        instance.updated_by = user
        instance.save()
        return instance

class PublisherSerializer(serializers.ModelSerializer):     
    token = serializers.CharField(write_only=True)     
    created_by = UserSerializer(read_only=True)
    updated_by = UserSerializer(read_only=True)
    class Meta:
        model = Publisher
        fields = (
            'id', 'name', 'description', 'created_by', 'created_at', 'updated_by', 'updated_at', 'token'           
        ) 

    def create(self, validated_data):                
        user = Token.objects.get(key=validated_data['token']).user                
        publisher = Publisher(
            name = validated_data['name'],
            description = validated_data['description'],
            created_by = user 
        )
        publisher.save()
        return publisher

    def update(self, instance, validated_data):                
        user = Token.objects.get(key=validated_data['token']).user   
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)     
        instance.updated_by = user
        instance.save()
        return instance

def isUndefined(data):
    if (data == 'undefined' or data == None):
        return True
    return False

class BookSerializer(serializers.ModelSerializer):         
    image = serializers.ImageField(required=False, use_url=True)  
    token = serializers.CharField(write_only=True)     
    file = serializers.FileField(write_only=True)
    category = CategorySerializer(many=True)
    author = AuthorSerializer(many=True)
    publisher = PublisherSerializer(many=True)
    created_by = UserSerializer(read_only=True)
    updated_by = UserSerializer(read_only=True) 

    class Meta:
        model = Book
        fields = (
            'id', 'name', 'code', 'description', 'category', 'author', 'publisher', 'published_at', 
            'pages', 'height', 'width', 'depth', 'weight', 'count', 'available', 'price', 'image', 
            'created_by', 'created_at', 'updated_by', 'updated_at', 'token', 'file'
        )     

class OrderSerializer(serializers.ModelSerializer):     
    token = serializers.CharField(write_only=True)     
    customer = ProfileSerializer()
    book = BookSerializer()
    created_by = UserSerializer(read_only=True)
    updated_by = UserSerializer(read_only=True)
    class Meta:
        model = Order
        fields = (
            'id', 'customer', 'book', 'description', 'count', 'day', 'returned', 'returned_at', 'created_by', 'created_at', 'updated_by', 'updated_at', 'token'            
        ) 

class VoteOptionSerializer(serializers.ModelSerializer):     
    token = serializers.CharField(write_only=True)         
    class Meta:
        model = VoteOption
        fields = (
            'id', 'name', 'count', 'created_by', 'created_at', 'token'            
        ) 

class VoteSerializer(serializers.ModelSerializer):     
    token = serializers.CharField(write_only=True)             
    class Meta:
        model = Vote
        fields = (
            'id', 'customer', 'selections', 'created_at', 'updated_at', 'token'            
        ) 

class VoteSelectSerializer(serializers.ModelSerializer):     
    token = serializers.CharField(write_only=True)         
    options = VoteOptionSerializer(many=True)
    votes = VoteSerializer(many=True)
    class Meta:
        model = VoteSelect
        fields = (
            'id', 'options', 'votes', 'created_by', 'created_at', 'token'            
        ) 
