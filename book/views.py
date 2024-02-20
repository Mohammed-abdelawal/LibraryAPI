from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.response import Response

from library.models import Borrower
from library.serializers import BorrowRecordSerializer
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [DjangoModelPermissions]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author__name', 'isbn']
    ordering_fields = ['title', 'publication_date']

    @action(methods=['POST'], detail=True, url_path='borrow_book')
    def borrow_book(self, request, pk=None):
        """Borrow a book."""
        book = self.get_object()
        borrower_pk = request.data.get('borrower_pk')
        if not borrower_pk:
            return Response({"detail": "Borrower primary key (borrower_pk) is required in the request data."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            borrower = Borrower.objects.get(pk=borrower_pk)
        except Borrower.DoesNotExist:
            return Response({"detail": "Borrower not found."}, status=status.HTTP_404_NOT_FOUND)

        if book.available_count < 1:
            return Response({"detail": "There are no books available for borrowing."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = BorrowRecordSerializer(data={"book": book.pk, "borrower": borrower.pk})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorViewSet(viewsets.ModelViewSet):
    """
    A view set for managing authors.

    This view set provides CRUD operations for authors in the library.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [DjangoModelPermissions]
