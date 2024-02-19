import random
from functools import partial

import factory

from book.models import Author, Book


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    name = factory.Sequence(lambda n: f'Author {n}')
    biography = factory.Faker("paragraph")
    birth_date = factory.Faker('date')
    death_date = factory.Faker('date')


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    title = factory.Sequence(lambda n: f'Book {n}')
    author = factory.SubFactory(AuthorFactory)
    isbn = factory.Sequence(lambda n: f"23{n}2-342-{n}"[:12])
    genre = factory.Faker("name")
    publication_date = factory.Faker('date')
    description = factory.Faker("sentence")
    total_count = factory.LazyFunction(partial(random.randint, 3, 100))
