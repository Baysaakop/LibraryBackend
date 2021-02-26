from datetime import datetime
from .models import Profile
from django.contrib.auth.models import User
from .serializers import UserSerializer, ProfileSerializer
from .models import Profile
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status, serializers, viewsets, filters

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']            

class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['code', 'verified']            

    def create(self, request, *args, **kwargs):                       
        user = Token.objects.get(key=request.data['token']).user   
        code = request.data['code']         
        if Profile.objects.filter(code=code).count() > 0:                    
            return Response(data="Хэрэглэгч аль хэдийн бүртгэлтэй байна.", status=status.HTTP_409_CONFLICT)
        else:            
            profile = Profile.objects.create(                
                code=request.data['code'],
                first_name=request.data['first_name'],
                last_name=request.data['last_name'],
                mobile=request.data['mobile'],                      
                description=request.data['description']
            )        
            profile.save()        
            serializer = ProfileSerializer(profile)
            headers = self.get_success_headers(serializer.data)        
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)    

    def update(self, request, *args, **kwargs):                         
        profile = self.get_object()                 
        user = Token.objects.get(key=request.data['token']).user            
        if 'role' in request.data:
            profile.role=request.data['role']                            
        if 'first_name' in request.data:
            profile.first_name=request.data['first_name'] 
        if 'last_name' in request.data:
            profile.last_name=request.data['last_name']   
        if 'mobile' in request.data:
            profile.mobile=request.data['mobile'] 
        if 'verified' in request.data:
            if request.data['verified'] == 'True':
                profile.verified = True
        # if 'birthday' in request.data:
        #     if str(request.data['birthday']) != "":
        #         profile.birthday=request.data['birthday']  
        if 'description' in request.data:
            profile.description=request.data['description']                
        profile.save()
        serializer = ProfileSerializer(profile)
        headers = self.get_success_headers(serializer.data)        
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)
