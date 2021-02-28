from django.contrib import admin
from .models import Profile, ResetRequest

admin.site.register(Profile)
admin.site.register(ResetRequest)
