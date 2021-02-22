from .views import CategoryViewSet, AuthorViewSet, PublisherViewSet, BookViewSet, OrderViewSet, VoteOptionViewSet, VoteViewSet, VoteSelectViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'authors', AuthorViewSet, basename='authors')
router.register(r'publishers', PublisherViewSet, basename='publishers')
router.register(r'books', BookViewSet, basename='books')
router.register(r'orders', OrderViewSet, basename='orders')
router.register(r'vote_options', VoteOptionViewSet, basename='vote_options')
router.register(r'votes', VoteViewSet, basename='votes')
router.register(r'vote_selects', VoteSelectViewSet, basename='vote_selects')
urlpatterns = router.urls