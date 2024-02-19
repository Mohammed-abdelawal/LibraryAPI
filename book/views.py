from rest_framework import viewsets, filters
from rest_framework.permissions import DjangoModelPermissions

from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [DjangoModelPermissions]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author__name', 'isbn']
    ordering_fields = ['title', 'publication_date']


class AuthorViewSet(viewsets.ModelViewSet):
    """
    A view set for managing authors.

    This view set provides CRUD operations for authors in the library.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [DjangoModelPermissions]
