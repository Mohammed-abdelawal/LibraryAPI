import factory
from faker import Faker

from book.models import Author, Book

fake = Faker()


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    name = factory.Sequence(lambda n: f'Author {n}')
    biography = fake.paragraph()
    birth_date = fake.date_of_birth()
    death_date = fake.date_of_death()


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    title = factory.Sequence(lambda n: f'Book {n}')
    author = factory.SubFactory(AuthorFactory)
    isbn = fake.unique.isbn13(separator="-")
    genre = fake.word()
    publication_date = fake.date_this_decade()
    description = fake.paragraph()
    total_count = fake.random_int(min=1, max=100)
