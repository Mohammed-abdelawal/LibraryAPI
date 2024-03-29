# Generated by Django 5.0.2 on 2024-02-19 17:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Phone Number')),
            ],
        ),
        migrations.CreateModel(
            name='BorrowRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrow_date', models.DateField(auto_now_add=True, verbose_name='Borrow Date')),
                ('return_date', models.DateField(blank=True, null=True, verbose_name='Return Date')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrow_records', to='book.book', verbose_name='Book')),
                ('borrower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrow_records', to='library.borrower', verbose_name='Borrower')),
            ],
        ),
    ]
