import datetime

from django.db import models
from django.db.models import Count


class BookManager(models.Manager):
    def get_queryset(self):
        # To avoid N+1 issue
        return super().get_queryset().annotate(borrowed_count=Count('borrow_records'))


class Author(models.Model):
    """Model representing an author."""
    name: str = models.CharField(max_length=255, verbose_name="Name")
    biography: str = models.TextField(blank=True, verbose_name="Biography")
    birth_date: datetime.date = models.DateField(null=True, blank=True, verbose_name="Birth Date")
    death_date: datetime.date = models.DateField(null=True, blank=True, verbose_name="Death Date")

    def __str__(self):
        """Return the name of the author."""
        return self.name


class Book(models.Model):
    """Model representing a book in the library."""
    title: str = models.CharField(max_length=255, verbose_name="Title")
    author: Author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, verbose_name="Author")
    isbn: str = models.CharField(max_length=13, unique=True, verbose_name="ISBN")
    genre: str = models.CharField(max_length=100, verbose_name="Genre")
    publication_date: datetime.date = models.DateField(verbose_name="Publication Date")
    description: str = models.TextField(verbose_name="Description")
    total_count: int = models.PositiveIntegerField(default=1, verbose_name="Total Count")

    objects = BookManager()

    @property
    def borrowed_count(self) -> int:
        """Calculate and return the count of borrowed books."""
        return self.borrowed_count

    @property
    def available_count(self) -> int:
        """Calculate and return the count of available books."""
        return self.total_count - self.borrowed_count

    def __str__(self) -> str:
        """Return the title of the book."""
        return self.title
