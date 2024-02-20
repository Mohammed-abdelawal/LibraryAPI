# Library Management System

This is a Django project for managing a library's book borrowing system. It allows users to perform CRUD operations on books and borrow records, as well as search and filter books, borrow books, and manage borrow records.

## Features

- CRUD Operations: Perform Create, Read, Update, and Delete operations on books and borrow records.
- Book Borrowing: Allow users to borrow available books from the library.
- Borrow Records Management: Track borrow records including borrower details, borrow dates, and return dates.
- Security Measures: Implement API security focusing on authentication and authorization using Django's built-in permissions system.
- Documentation: Provide comprehensive documentation for the API endpoints, including parameters, usage examples, and expected responses.

## Key Components

- Django: Web framework for building the backend of the application.
- Django REST Framework: Toolkit for building Web APIs in Django.
- PostgreSQL: Database system used to store data.
- Factory Boy: Library for creating test data in tests.
- Pytest: Testing framework for writing and running tests.
- Postman: API client for testing API endpoints.

## Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/yourusername/library-management-system.git
```
Navigate to the project directory:
```bash
cd LibraryAPI
```

Copy the .env.example file to .env:
```bash
cp .env.example .env
```

Open the .env file and configure its contents:
Make sure to set the appropriate values for SECRET_KEY, DATABASE_HOST, DATABASE_PORT, DATABASE_NAME, DATABASE_USER, and DATABASE_PASSWORD according to your development environment.

```makefile
SECRET_KEY=secret-123456

DATABASE_HOST=0.0.0.0
DATABASE_PORT=5432
DATABASE_NAME=library
DATABASE_USER=postgres
DATABASE_PASSWORD=000000000

DEBUG=False

LANGUAGE_CODE=en-us
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Set up the database:

```bash
python manage.py migrate
```

Create a superuser:

```bash
python manage.py createsuperuser
```

Start the development server:

```bash
python manage.py runserver
```


Access the API in your web browser or API client at http://localhost:8000/api/v1/book-app and http://localhost:8000/api/v1/library-app