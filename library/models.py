import datetime

from django.db import models

from book.models import Book


class Borrower(models.Model):
    """Model representing individuals borrowing books."""
    name: str = models.CharField(max_length=100, verbose_name="Name")
    email: str = models.EmailField(unique=True, verbose_name="Email")
    phone_number: str = models.CharField(max_length=20, verbose_name="Phone Number")

    def __str__(self) -> str:
        """Return the name of the borrower."""
        return self.name


class BorrowRecord(models.Model):
    """Model representing a record of book borrowings."""
    book: Book = models.ForeignKey(
        Book, on_delete=models.CASCADE,
        verbose_name="Book", related_name="borrow_records"
    )
    borrower: Borrower = models.ForeignKey(
        Borrower, on_delete=models.CASCADE,
        verbose_name="Borrower", related_name="borrow_records"
    )
    borrow_date: datetime.date = models.DateField(auto_now_add=True, verbose_name="Borrow Date")
    return_date: datetime.date = models.DateField(null=True, blank=True, verbose_name="Return Date")

    def __str__(self) -> str:
        """Return a string representation of the borrowing record."""
        return f"{self.borrower.name} borrows {self.book.title}"
