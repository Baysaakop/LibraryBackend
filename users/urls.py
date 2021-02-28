from .views import UserViewSet, ProfileViewSet, ResetRequestViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'customers', ProfileViewSet, basename='customers')
router.register(r'resetrequests', ResetRequestViewSet, basename='resetrequests')
urlpatterns = router.urls