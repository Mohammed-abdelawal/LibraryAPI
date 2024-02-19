from django.urls import path, include
from rest_framework.routers import DefaultRouter

from book import views

router = DefaultRouter()
router.register('books', views.BookViewSet)
router.register('authors', views.AuthorViewSet)

urlpatterns = [
    path('', include(router.urls))
]