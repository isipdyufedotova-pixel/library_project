from django import forms
from .models import Book, Author, Publisher, Reader, Loan


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'description', 'year', 'isbn', 'photo',
                  'is_exists', 'category', 'author', 'publisher']


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'description', 'photo']


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name', 'city', 'logo']


class ReaderForm(forms.ModelForm):
    class Meta:
        model = Reader
        fields = ['name', 'ticket_number', 'photo', 'faculty']


class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['book', 'reader', 'taken_at', 'due_at', 'returned']