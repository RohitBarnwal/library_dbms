
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='book-list'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='author-list'),
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),
    path('members/', views.MemberListView.as_view(), name='member-list'),
    path('member/<int:pk>/', views.MemberDetailView.as_view(), name='member-detail'),
    path('loans/', views.LoanListView.as_view(), name='loan-list'),
    path('loan/<int:pk>/', views.LoanDetailView.as_view(), name='loan-detail'),
]
