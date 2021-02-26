from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile
from allauth.account import app_settings as allauth_settings
from allauth.utils import get_username_max_length
from allauth.account.utils import setup_user_email
from allauth.account.adapter import get_adapter

class ProfileSerializer(serializers.ModelSerializer):        
    class Meta:
        model = Profile
        # fields = (
        #     'id', 'description', 'phone_number', 'birth_date', 'avatar', 'role'
        # )
        read_only_fields = ('created_at', 'updated_at', 'role')        
        exclude = ('user',)
     
class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=False)
    class Meta:
        model = User
        fields = (
            'id', 'username', 'first_name', 'last_name', 'profile'
        )

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=get_username_max_length(),
        min_length=allauth_settings.USERNAME_MIN_LENGTH,
        required=allauth_settings.USERNAME_REQUIRED
    )
    first_name = serializers.CharField(required=True, write_only=True)
    last_name = serializers.CharField(required=True, write_only=True)
    password1 = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)

    def validate_username(self, username):
        username = get_adapter().clean_username(username)
        return username

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(
                _("The two password fields didn't match."))
        return data

    def get_cleaned_data(self):
        return {
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'password1': self.validated_data.get('password1', ''),
            'username': self.validated_data.get('username', ''),
            'email': self.validated_data.get('email', ''),
        }

    def save(self, request):        
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)        
        user.profile.save()        
        return user