from rest_framework import serializers

from book.models import Book
from .models import Borrower, BorrowRecord


class BorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrower
        fields = ['id', 'name', 'email', 'phone_number']
        read_only_fields = ('id', 'borrowed_books')

    def get_borrowed_books(self, instance: Borrower):
        borrow_records = BorrowRecord.objects.filter(borrower=instance, return_date=None)
        serializer = BorrowRecordSerializer(borrow_records, many=True)
        return serializer.data


class BorrowRecordSerializer(serializers.ModelSerializer):
    borrower = serializers.PrimaryKeyRelatedField(queryset=Borrower.objects.all())
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())

    class Meta:
        model = BorrowRecord
        fields = ['id', 'book', 'borrower', 'borrow_date', 'return_date']
