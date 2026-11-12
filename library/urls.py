from django.urls import path
from .views import *

urlpatterns = [
    path('info', info_view),
    path('', info_view),

    # Books
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/<int:pk>', BookDetailView.as_view(), name='book_detail'),
    path('books/create/', BookCreateView.as_view(), name='book_create'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book_update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),

    # Authors
    path('authors/', AuthorListView.as_view(), name='author_list'),
    path('authors/<int:pk>', AuthorDetailView.as_view(), name='author_detail'),
    path('authors/create/', AuthorCreateView.as_view(), name='author_create'),
    path('authors/<int:pk>/update/', AuthorUpdateView.as_view(), name='author_update'),
    path('authors/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author_delete'),

    # Publishers
    path('publishers/', PublisherListView.as_view(), name='publisher_list'),
    path('publishers/<int:pk>', PublisherDetailView.as_view(), name='publisher_detail'),
    path('publishers/create/', PublisherCreateView.as_view(), name='publisher_create'),
    path('publishers/<int:pk>/update/', PublisherUpdateView.as_view(), name='publisher_update'),
    path('publishers/<int:pk>/delete/', PublisherDeleteView.as_view(), name='publisher_delete'),

    # Readers
    path('readers/', ReaderListView.as_view(), name='reader_list'),
    path('readers/<int:pk>', ReaderDetailView.as_view(), name='reader_detail'),
    path('readers/create/', ReaderCreateView.as_view(), name='reader_create'),
    path('readers/<int:pk>/update/', ReaderUpdateView.as_view(), name='reader_update'),
    path('readers/<int:pk>/delete/', ReaderDeleteView.as_view(), name='reader_delete'),

    # Loans
    path('loans/', LoanListView.as_view(), name='loan_list'),
    path('loans/<int:pk>', LoanDetailView.as_view(), name='loan_detail'),
    path('loans/create/', LoanCreateView.as_view(), name='loan_create'),
    path('loans/<int:pk>/update/', LoanUpdateView.as_view(), name='loan_update'),
    path('loans/<int:pk>/delete/', LoanDeleteView.as_view(), name='loan_delete'),

    # Дополнительные
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('faculties/', FacultyListView.as_view(), name='faculty_list'),
    path('reviews/', ReviewListView.as_view(), name='review_list'),
]