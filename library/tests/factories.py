import factory

from book.tests.factories import BookFactory
from library.models import Borrower, BorrowRecord


class BorrowerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Borrower

    name = factory.Faker("name")
    email = factory.Sequence(lambda n: f'{n}user@example.com')
    phone_number = factory.Sequence(lambda n: f"01013884364{n}")


class BorrowRecordFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BorrowRecord

    book = factory.SubFactory(BookFactory)
    borrower = factory.SubFactory(BorrowerFactory)
    borrow_date = factory.Faker('date')
    return_date = factory.Faker('date')
