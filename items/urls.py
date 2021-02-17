from .views import ItemViewSet, CategoryViewSet, AuthorViewSet, PublisherViewSet, CustomerViewSet, BookViewSet, OrderViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'items', ItemViewSet, basename='items')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'authors', AuthorViewSet, basename='authors')
router.register(r'publishers', PublisherViewSet, basename='publishers')
router.register(r'customers', CustomerViewSet, basename='customers')
router.register(r'books', BookViewSet, basename='books')
router.register(r'orders', OrderViewSet, basename='orders')
urlpatterns = router.urls