from .views import UserViewSet, ProfileViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'customers', ProfileViewSet, basename='customers')
urlpatterns = router.urls