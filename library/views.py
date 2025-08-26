from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book, Author, Member, Loan

def index(request):
    return render(request, 'library/index.html')

class BookListView(ListView):
    model = Book
    template_name = 'library/book_list.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    template_name = 'library/book_detail.html'
    context_object_name = 'book'

class AuthorListView(ListView):
    model = Author
    template_name = 'library/author_list.html'
    context_object_name = 'authors'

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'library/author_detail.html'
    context_object_name = 'author'

class MemberListView(ListView):
    model = Member
    template_name = 'library/member_list.html'
    context_object_name = 'members'

class MemberDetailView(DetailView):
    model = Member
    template_name = 'library/member_detail.html'
    context_object_name = 'member'

class LoanListView(ListView):
    model = Loan
    template_name = 'library/loan_list.html'
    context_object_name = 'loans'

class LoanDetailView(DetailView):
    model = Loan
    template_name = 'library/loan_detail.html'
    context_object_name = 'loan'