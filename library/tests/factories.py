import factory
from faker import Faker

from book.tests.factories import BookFactory
from library.models import Borrower, BorrowRecord

fake = Faker()


class BorrowerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Borrower

    name = factory.Sequence(lambda n: f'Borrower {n}')
    email = factory.LazyAttribute(lambda obj: f'{obj.name.replace(" ", "_").lower()}@example.com')
    phone_number = fake.phone_number()


class BorrowRecordFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BorrowRecord

    book = factory.SubFactory(BookFactory)
    borrower = factory.SubFactory(BorrowerFactory)
    borrow_date = fake.date_this_decade()
    return_date = factory.LazyAttribute(lambda obj: fake.date_between(start_date=obj.borrow_date))
