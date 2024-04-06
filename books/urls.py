from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .serializers import BookViewSet, BookClubViewSet, DiscussionViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'clubs', BookClubViewSet)
router.register(r'discussions', DiscussionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]