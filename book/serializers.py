from rest_framework import serializers

from .models import Book, Author


class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
    borrowed_count = serializers.IntegerField()

    class Meta:
        model = Book
        fields = [
            'id', 'title', 'author', 'isbn', 'genre',
            'publication_date', 'description', 'total_count',
            'available_count', 'borrowed_count'
        ]
        read_only_fields = ('id', 'borrowed_count', "available_count")


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'biography', 'birth_date', 'death_date']
        read_only_fields = ('id', 'books')

        def get_books(self, instance: Author):
            books = Book.objects.filter(author=instance)
            serializer = BookSerializer(books, many=True)
            return serializer.data
