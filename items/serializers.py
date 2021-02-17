from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Item, Author, Category, Publisher, Book, Customer, Order, User

class ItemSerializer(serializers.ModelSerializer):
    token = serializers.CharField(write_only=True)        
    image = serializers.ImageField(required=False, use_url=True)
    class Meta:
        model = Item
        fields = ('id', 'name', 'description', 'image', 'created_by', 'updated_by', 'created_at', 'updated_at', 'token')        
    
    def create(self, validated_data):                
        user = Token.objects.get(key=validated_data['token']).user                
        item = Item(
            name=validated_data['name'],
            description=validated_data['description'],
            created_by=user 
        )
        item.save()
        return item

    def update(self, instance, validated_data):                
        user = Token.objects.get(key=validated_data['token']).user   
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.updated_by = user
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):    
    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'first_name', 'last_name', 'profile'
        )

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

class CustomerSerializer(serializers.ModelSerializer):    
    token = serializers.CharField(write_only=True)     
    created_by = UserSerializer(read_only=True)
    updated_by = UserSerializer(read_only=True)
    class Meta:
        model = Customer
        fields = (
            'id', 'name', 'code', 'mobile', 'birthday', 'description', 'created_by', 'created_at', 'updated_by', 'updated_at', 'token'
        )

    def create(self, validated_data):                
        user = Token.objects.get(key=validated_data['token']).user                
        customer = Customer(
            name = validated_data['name'],
            code = validated_data['code'],
            mobile = validated_data['mobile'],
            birthday = validated_data['birthday'],
            description = validated_data['description'],
            created_by = user 
        )
        customer.save()
        return customer

    def update(self, instance, validated_data):                
        user = Token.objects.get(key=validated_data['token']).user   
        instance.name = validated_data.get('name', instance.name)
        instance.code = validated_data.get('code', instance.code)
        instance.mobile = validated_data.get('mobile', instance.mobile)
        instance.birthday = validated_data.get('birthday', instance.birthday)
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
            'created_by', 'created_at', 'updated_by', 'updated_at', 'token'
        )     

class OrderSerializer(serializers.ModelSerializer):     
    token = serializers.CharField(write_only=True)     
    customer = CustomerSerializer()
    book = BookSerializer()
    created_by = UserSerializer(read_only=True)
    updated_by = UserSerializer(read_only=True)
    class Meta:
        model = Order
        fields = (
            'id', 'customer', 'book', 'description', 'count', 'day', 'created_by', 'created_at', 'updated_by', 'updated_at', 'token'            
        ) 

