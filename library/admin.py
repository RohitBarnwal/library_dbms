from django.contrib import admin
from .models import Member, Staff, Publisher, Author, Book, BookAuthor, Loan, LoanDetail

admin.site.register(Member)
admin.site.register(Staff)
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookAuthor)
admin.site.register(Loan)
admin.site.register(LoanDetail)