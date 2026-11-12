from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import *
from .forms import BookForm, AuthorForm, PublisherForm, ReaderForm, LoanForm


def info_view(request):
    return render(request, 'info.html')


# ---------------- BOOK ----------------
class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'books'


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book_list')


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book_list')


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = reverse_lazy('book_list')


# ---------------- AUTHOR ----------------
class AuthorListView(ListView):
    model = Author
    template_name = 'authors/author_list.html'
    context_object_name = 'authors'


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'authors/author_detail.html'
    context_object_name = 'authors'


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'authors/author_form.html'
    success_url = reverse_lazy('author_list')


class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'authors/author_form.html'
    success_url = reverse_lazy('author_list')


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'authors/author_confirm_delete.html'
    success_url = reverse_lazy('author_list')


# ---------------- PUBLISHER ----------------
class PublisherListView(ListView):
    model = Publisher
    template_name = 'publishers/publisher_list.html'
    context_object_name = 'publishers'


class PublisherDetailView(DetailView):
    model = Publisher
    template_name = 'publishers/publisher_detail.html'
    context_object_name = 'publishers'


class PublisherCreateView(CreateView):
    model = Publisher
    form_class = PublisherForm
    template_name = 'publishers/publisher_form.html'
    success_url = reverse_lazy('publisher_list')


class PublisherUpdateView(UpdateView):
    model = Publisher
    form_class = PublisherForm
    template_name = 'publishers/publisher_form.html'
    success_url = reverse_lazy('publisher_list')


class PublisherDeleteView(DeleteView):
    model = Publisher
    template_name = 'publishers/publisher_confirm_delete.html'
    success_url = reverse_lazy('publisher_list')


# ---------------- READER ----------------
class ReaderListView(ListView):
    model = Reader
    template_name = 'readers/reader_list.html'
    context_object_name = 'readers'


class ReaderDetailView(DetailView):
    model = Reader
    template_name = 'readers/reader_detail.html'
    context_object_name = 'readers'


class ReaderCreateView(CreateView):
    model = Reader
    form_class = ReaderForm
    template_name = 'readers/reader_form.html'
    success_url = reverse_lazy('reader_list')


class ReaderUpdateView(UpdateView):
    model = Reader
    form_class = ReaderForm
    template_name = 'readers/reader_form.html'
    success_url = reverse_lazy('reader_list')


class ReaderDeleteView(DeleteView):
    model = Reader
    template_name = 'readers/reader_confirm_delete.html'
    success_url = reverse_lazy('reader_list')


# ---------------- LOAN ----------------
class LoanListView(ListView):
    model = Loan
    template_name = 'loans/loan_list.html'
    context_object_name = 'loans'


class LoanDetailView(DetailView):
    model = Loan
    template_name = 'loans/loan_detail.html'
    context_object_name = 'loans'


class LoanCreateView(CreateView):
    model = Loan
    form_class = LoanForm
    template_name = 'loans/loan_form.html'
    success_url = reverse_lazy('loan_list')


class LoanUpdateView(UpdateView):
    model = Loan
    form_class = LoanForm
    template_name = 'loans/loan_form.html'
    success_url = reverse_lazy('loan_list')


class LoanDeleteView(DeleteView):
    model = Loan
    template_name = 'loans/loan_confirm_delete.html'
    success_url = reverse_lazy('loan_list')


# ---------------- ДОПОЛНИТЕЛЬНО ----------------
class CategoryListView(ListView):
    model = Category
    template_name = 'categories/category_list.html'
    context_object_name = 'categories'


class FacultyListView(ListView):
    model = Faculty
    template_name = 'faculties/faculty_list.html'
    context_object_name = 'faculties'


class ReviewListView(ListView):
    model = Review
    template_name = 'reviews/review_list.html'
    context_object_name = 'reviews'