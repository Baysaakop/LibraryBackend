from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('rest-auth/', include('rest_auth.urls')),    
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path("api/items/", include('items.urls')),
    path("api/users/", include('users.urls'))    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
